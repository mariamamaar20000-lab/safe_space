import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Safe Space | Dr. Sharon", page_icon="🌿", layout="centered")

# التصميم الفخم
st.markdown("""
    <style>
    .stApp { background-color: #0b1120; color: white; }
    .main-title { font-size: 35px; color: #38bdf8; text-align: center; font-weight: bold; }
    .chat-bubble { background-color: #1e293b; padding: 20px; border-radius: 15px; border-right: 5px solid #38bdf8; margin-top: 15px; font-size: 18px; line-height: 1.7; }
    .whatsapp-btn { background: linear-gradient(90deg, #25d366, #128c7e) !important; color: white !important; border-radius: 15px; padding: 12px; text-decoration: none; display: block; text-align: center; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown('<div class="main-title">🌿 Safe Space | Dr. Sharon</div>', unsafe_allow_html=True)

# عرض شات متصل (الذاكرة)
for msg in st.session_state.messages:
    role = "أنت" if msg["role"] == "user" else "د. شارون"
    st.markdown(f'<div class="chat-bubble"><b>{role}:</b> {msg["content"]}</div>', unsafe_allow_html=True)

# عقل دكتور شارون (الردود الذكية بالمصري والدين)
def get_intelligent_response(text):
    text = text.lower()
    
    # 1. منع الانتحار بوازع ديني ونفسي
    if any(word in text for word in ["انتحر", "اموت", "انهي حياتي", "اقتل نفسي"]):
        return """يا صديقي، استغفر الله العظيم.. الدنيا مهما اسودت فهي دار اختبار، وروحك دي أمانة عندك مش ملكك عشان تنهيها. ربنا بيقول "وَلَا تَقْتُلُوا أَنفُسَكُمْ ۚ إِنَّ اللَّهَ كَانَ بِكُمْ رَحِيمًا". 
        الوجع اللي حاسس بيه دلوقتي صدقني هيعدي، وكل ضيقة وليها مخرج. بلاش تضيع آخرتك ودنيتك في لحظة يأس. أنا جنبك وسامعك، احكي لي إيه اللي وصلك لكدة؟ خلينا نلاقي حل سوا، والموت عمره ما كان حل. كلمني واتساب حالاً لو حاسس إنك مش قادر! ❤️🙏"""

    # 2. مشاكل الأهل (الاحتواء والبر)
    elif "أهل" in text or "اهل" in text or "بابا" in text or "ماما" in text:
        return """الأهل هما أصعب وأهم علاقة.. مفيش حد بيحبك قدهم حتى لو طريقتهم غلط أو خنقتك. النبي وصانا بالبر حتى لو في اختلاف. 
        بس أنا عايز أعرف منك: إيه أكتر موقف النهاردة خلاك تحس إنك مش طايقهم؟ احكي لي بالتفصيل هما عملوا إيه؟ أنا سامعك ومش هحكم عليك، هنفهم سوا إزاي نتعامل معاهم من غير ما نتعب نفسياً. 🏠🫂"""

    # 3. الفشل واليأس
    elif any(word in text for word in ["فشلت", "خسرت", "ضعت"]):
        return "الوقوع مش عيب، العيب إننا مانقومش. ربنا بيقفل باب عشان يفتح عشرة أحسن منه. قولي بس إيه اللي حصل وخلاك تحس بالفشل ده؟ خلينا نحلل الموقف ونطلع منه بدرس يقويك. أنت قدها! ✨💪"

    # رد عام ذكي (بيحلل سياق الكلام)
    elif len(text) > 15:
        return "كلامك عميق ومحتاج وقفة.. أنا حاسس بكل حرف كتبته. كمل فضفضة وقولي إيه أكتر تفصيلة واجعاك في الحكاية دي؟ أنا مركز معاك جداً يا بطل. 😊🌿"
    
    else:
        return "أنا معاك وسامعك بكل اهتمام.. فضفض وطلع اللي في قلبك كله، أنا دكتورك وصديقك. ❤️"

# منطقة الإدخال
with st.form("chat_input", clear_on_submit=True):
    u_input = st.text_input("احكي اللي جواك (دكتور شارون سامعك)...")
    submit = st.form_submit_button("إرسال")

if submit and u_input:
    st.session_state.messages.append({"role": "user", "content": u_input})
    with st.spinner("دكتور شارون بيفكر في أنسب رد ليك..."):
        time.sleep(1.5)
        ans = get_intelligent_response(u_input)
        st.session_state.messages.append({"role": "dr", "content": ans})
    st.rerun()

# الأزرار والدعم
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("✨ رسالة تحفيز"):
        st.info("أنت النهاردة أقوى من امبارح لمجرد إنك قررت تتكلم. كمل طريقك!")
with col2:
    if st.button("🗑️ ابدأ جلسة جديدة"):
        st.session_state.messages = []
        st.rerun()

st.markdown(f'<a href="https://wa.me/201009469831" target="_blank" class="whatsapp-btn">📞 ابعت رسالة خاصة لدكتور شارون (واتساب)</a>', unsafe_allow_html=True)
