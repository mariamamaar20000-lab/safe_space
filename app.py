import streamlit as st
import time
from textblob import TextBlob
from openai import OpenAI

# ================= API =================
client = OpenAI(api_key="PUT_YOUR_API_KEY_HERE")

# ================= UI =================
st.set_page_config("Safe Space | Dr. Sharon", "🧠", layout="centered")

st.markdown("""
<style>
.stApp { background:#020617; color:white }
.title { font-size:38px; color:#38bdf8; text-align:center; font-weight:800 }
.box { background:#020617; border:1px solid #1e293b; padding:20px; border-radius:18px; margin:12px 0 }
.user { border-right:6px solid #22c55e }
.bot { border-right:6px solid #38bdf8 }
.alert { border-right:6px solid #ef4444; background:#160000 }
.small { color:#94a3b8; font-size:14px }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧠 Safe Space | Dr. Sharon</div>', unsafe_allow_html=True)

# ================= MEMORY =================
if "chat" not in st.session_state:
    st.session_state.chat = []

if "patterns" not in st.session_state:
    st.session_state.patterns = []

# ================= PSYCHO ENGINE =================
def psycho_scan(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    danger_words = ["انتحر", "اموت", "مش عايش", "عايز اختفي", "أأذي نفسي"]
    danger = any(w in text.lower() for w in danger_words)

    if danger:
        risk = "HIGH 🚨"
    elif polarity < -0.5:
        risk = "MEDIUM ⚠️"
    else:
        risk = "LOW 🟢"

    if polarity < -0.6:
        state = "اكتئاب / ضغط نفسي عالي"
    elif polarity < -0.2:
        state = "قلق أو توتر"
    elif polarity > 0.4:
        state = "مزاج إيجابي"
    else:
        state = "مزاج متقلب"

    return state, risk

# ================= SMART QUESTION =================
def smart_question(state):
    if "قلق" in state:
        return "الإحساس ده بيجيلك فجأة ولا بعد تفكير طويل؟"
    if "اكتئاب" in state:
        return "حاسس بكده من إمتى؟ ولا الموضوع له سبب قريب؟"
    return "خلّينا نركز… إيه أكتر نقطة شاغلاك دلوقتي؟"

# ================= DEEP PSYCHO PROFILE =================
def deep_psycho_profile(text):
    t = text.lower()
    score = 50
    traits = []

    if any(x in t for x in ["دايما", "عمري", "مفيش فايده"]):
        traits.append("تفكير أبيض/أسود")
        score -= 10
    if any(x in t for x in ["لو", "يمكن", "مش عارف"]):
        traits.append("تردد وقلق")
        score -= 5
    if any(x in t for x in ["زهقت", "تعبت", "مش قادر"]):
        traits.append("إرهاق نفسي")
        score -= 15
    if any(x in t for x in ["هحاول", "لازم", "هقوم"]):
        traits.append("إرادة مقاومة")
        score += 10

    score = max(0, min(100, score))
    return traits, score

# ================= THERAPY EXERCISE =================
def therapy_exercise(state):
    if "اكتئاب" in state:
        return "خلينا ناخد نفس سوا: خد شهيق 4 ثواني… ثبّت 4… زفير 6. كرر 3 مرات."
    elif "قلق" in state:
        return "بص حواليك وسمّي 5 حاجات شايفها، 3 أصوات سامعها، حاجة واحدة لامسها."
    else:
        return "أنت ثابت دلوقتي، حاول تكتب إحساسك في جملة واحدة من غير تفكير."

# ================= REMEMBER PATTERN =================
def remember_pattern(traits):
    for t in traits:
        if t not in st.session_state.patterns:
            st.session_state.patterns.append(t)

# ================= SILENCE LOGIC =================
def should_be_silent(text):
    return len(text.split()) < 4 or text.endswith("...")

# ================= AI BRAIN =================
def dr_sharon_ai(user_text, state, risk):
    traits, score = deep_psycho_profile(user_text)
    remember_pattern(traits)
    exercise = therapy_exercise(state)

    memory_note = ""
    if st.session_state.patterns:
        memory_note = f"خد بالك… ده مش أول مرة يطلع عندك {st.session_state.patterns[-1]}."

    if should_be_silent(user_text):
        return "أنا ساكت قصد… خُد وقتك. أنا موجود.", traits, score, exercise, memory_note

    system_prompt = f"""
أنت Dr. Sharon
دكتور نفسي رجل
بتتكلم مصري طبيعي جدًا
كلامك بسيط، واقعي، مش فيك
بتسأل بس لما السؤال مهم
أحيانًا تسكت لو السكوت أحسن
بتفتكر الأنماط مش الكلام
ما بتحكمش
ما تديش حلول جاهزة
خليك بني آدم قبل ما تكون دكتور
الحالة النفسية: {state}
مستوى الخطر: {risk}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        temperature=0.9
    )

    return response.choices[0].message.content, traits, score, exercise, memory_note

# ================= CHAT VIEW =================
for m in st.session_state.chat:
    css = "alert" if m.get("alert") else ("user" if m["role"]=="user" else "bot")
    name = "أنت" if m["role"]=="user" else "د. شارون"
    st.markdown(
        f'<div class="box {css}"><b>{name}:</b> {m["text"]}<br><span class="small">{m.get("meta","")}</span></div>',
        unsafe_allow_html=True
    )

# ================= INPUT =================
with st.form("input", clear_on_submit=True):
    text = st.text_input("اتكلم… كل اللي جواك آمن هنا")
    send = st.form_submit_button("إرسال")

if send and text:
    state, risk = psycho_scan(text)
    reply, traits, score, exercise, memory_note = dr_sharon_ai(text, state, risk)

    st.session_state.chat.append({
        "role":"user",
        "text":text,
        "meta":f"🧠 الحالة: {state} | ⚠️ الخطر: {risk}"
    })

    st.session_state.chat.append({
        "role":"bot",
        "text":reply,
        "meta":f"📊 تحليل: {state} | 🧬 سمات: {', '.join(traits)} | 📈 المؤشر: {score}/100 | 🧘 تمرين: {exercise}\n{memory_note}",
        "alert": True if "HIGH" in risk else False
    })

    st.rerun()

# ================= RESET =================
if st.button("🗑️ جلسة جديدة"):
    st.session_state.chat = []
    st.session_state.patterns = []
    st.rerun()
