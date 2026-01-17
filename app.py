import streamlit as st
import time
import random

# ================= UI & STYLE =================
st.set_page_config(page_title="Safe Space | Dr. Sharon", page_icon="🧠", layout="centered")

st.markdown("""
<style>
.stApp { background:#0b1120; color:white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
.title { font-size:40px; color:#38bdf8; text-align:center; font-weight:800; padding:20px; text-shadow: 2px 2px 4px #000; }
.box { background:#1e293b; border:1px solid #334155; padding:20px; border-radius:18px; margin:15px 0; line-height:1.6; position: relative; }
.user { border-right:6px solid #22c55e; background:#1e293b; }
.bot { border-right:6px solid #38bdf8; background:#0f172a; }
.alert { border-right:6px solid #ef4444; background:#2d0a0a; }
.small { color:#94a3b8; font-size:13px; margin-top:10px; display:block; border-top: 1px dashed #334155; padding-top:5px; }
.whatsapp-btn { background: #25d366; color: white !important; border-radius: 12px; padding: 10px; text-decoration: none; display: block; text-align: center; font-weight: bold; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧠 Safe Space | Dr. Sharon</div>', unsafe_allow_html=True)

# ================= MEMORY =================
if "chat" not in st.session_state:
    st.session_state.chat = []
if "patterns" not in st.session_state:
    st.session_state.patterns = []

# ================= SMART ENGINE (FREE VERSION) =================
def psycho_scan(text):
    t = text.lower()
    danger_words = ["انتحر", "اموت", "انهي حياتي", "أدبح", "أقتل نفسي", "سم", "حبوب"]
    danger = any(w in t for w in danger_words)
    
    if danger:
        return "اكتئاب حاد / خطر", "HIGH 🚨"
    if any(w in t for w in ["زهقت", "تعبت", "مخنوق", "اهلي", "البيت"]):
        return "ضغط نفسي / اجتماعي", "MEDIUM ⚠️"
    return "تفريغ مشاعر", "LOW 🟢"

def get_dr_sharon_response(text, state, risk):
    t = text.lower()
    
    # ردود ذكية جداً ومحللة للموقف (بالمصري)
    if risk == "HIGH 🚨":
        return "اسمعني يا بطل.. أنا حاسس بالوجع اللي أنت فيه، بس روحك دي أمانة وما ينفعش نفرط فيها مهما حصل. ربنا بيقول 'ولا تقتلوا أنفسكم إن الله كان بكم رحيماً'. استهدي بالله كدة وكلمني واتساب حالاً نلاقي مخرج سوا. الموت مش حل، ده هروب من فرصة إنك تبقى أحسن."

    if "اهل" in t or "بيت" in t or "بابا" in t or "ماما" in t:
        return "الأهل هما أكتر ناس بنحبهم وعشان كدة هما أكتر ناس بيقدروا يوجعونا. ما تسبش البيت ولا تاخد قرار وأنت متعصب. قولي بالظبط، إيه اللي حصل النهاردة وصلك للدرجة دي؟ أنا سامعك وبفهمك."

    if "فشلت" in t or "خسرت" in t or "سقطت" in t:
        return "الوقوع مش نهاية العالم، ده مجرد درس قاسي. أنت لسه جواك طاقة وقوة بدليل إنك جيت واتكلمت. إيه اللي أنت شايفه دلوقتي ممكن نعمله عشان نقوم تاني؟"

    if len(text) < 10:
        return "خُد وقتك.. أنا مش مستعجل. كمل كلامك وأنا معاك وبسمعك بقلبي قبل عقلي."

    # رد عام ذكي
    responses = [
        "كلامك فيه تفاصيل توجع، بس أنت شجاع إنك حكيت. كمل أنا بربط الخيوط ببعضها عشان نفهم المشكلة من جدرها.",
        "واضح إنك شايل كتير فوق طاقتك. قولي، إيه أكتر حاجة في اللي حكيته ده هي اللي مأثرة على نومك وتفكيرك دلوقتي؟",
        "أنا معاك.. الفضفضة دي أول خطوة في العلاج. احكي لي أكتر عن إحساسك في اللحظة دي."
    ]
    return random.choice(responses)

# ================= CHAT VIEW =================
chat_placeholder = st.container()
with chat_placeholder:
    for m in st.session_state.chat:
        css = "alert" if m.get("alert") else ("user" if m["role"]=="user" else "bot")
        name = "أنت" if m["role"]=="user" else "د. شارون"
        st.markdown(
            f'<div class="box {css}"><b>{name}:</b> {m["text"]}<br><span class="small">{m.get("meta","")}</span></div>',
            unsafe_allow_html=True
        )

# ================= INPUT =================
with st.form("chat_input", clear_on_submit=True):
    user_text = st.text_input("فضفض.. دكتور شارون معاك وفي سرية تامة")
    submitted = st.form_submit_button("إرسال")

if submitted and user_text:
    state, risk = psycho_scan(user_text)
    reply = get_dr_sharon_response(user_text, state, risk)
    
    # إضافة لليوزر
    st.session_state.chat.append({
        "role": "user",
        "text": user_text,
        "meta": f"🧠 الحالة: {state} | ⚠️ الخطر: {risk}"
    })
    
    # إضافة للدكتور
    st.session_state.chat.append({
        "role": "bot",
        "text": reply,
        "meta": f"📊 دكتور شارون بيحلل حالتك الآن...",
        "alert": True if risk == "HIGH 🚨" else False
    })
    st.rerun()

# ================= TOOLS =================
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("🗑️ جلسة جديدة"):
        st.session_state.chat = []
        st.rerun()
with col2:
    st.markdown('<a href="https://wa.me/201009469831" class="whatsapp-btn">📞 واتساب د. شارون</a>', unsafe_allow_html=True)
