import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Safe Space | Dr. Sharon", page_icon="🌿", layout="centered")

# التصميم الكحلي الفخم مع لمسات احترافية
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .main-title { font-size: 35px; color: #38bdf8; text-align: center; font-weight: bold; margin-bottom: 20px; }
    .chat-container { background-color: #1e293b; padding: 15px; border-radius: 15px; margin-bottom: 10px; border-right: 4px solid #38bdf8; }
    .user-msg { color: #f8fafc; font-weight: bold; margin-bottom: 5px; }
    .dr-msg { color: #38bdf8; margin-bottom: 15px; font-style: italic; }
    .stButton>button { border-radius: 20px; font-weight: bold; width: 100%; transition: 0.3s; }
    .whatsapp-btn { background: linear-gradient(90deg, #25d366, #128c7e) !important; color: white !important; height: 50px; font-size: 18px !important; }
    </style>
    """, unsafe_allow_html=True)

# تفعيل الذاكرة (عشان الشات ما يتمسحش)
if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown('<div class="main-title">🌿 Safe Space | Dr. Sharon</div>', unsafe_allow_html=True)

# عرض الشات القديم والجديد
chat_placeholder = st.container()
with chat_placeholder:
    for msg in st.session_state.messages:
        role = "أنت" if msg["role"] == "user" else "د. شارون"
        style = "user-msg" if msg["role"] == "user" else "dr-msg"
        st.markdown(f'<div class="chat-container"><div class="{style}">{role}: {msg["content"]}</div></div>', unsafe_allow_html=True)

# منطقة الإدخال
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("احكي اللي جواك هنا...", placeholder="أنا سامعك..")
    submit = st.form_submit_button("إرسال")

# منطق الردود الاحترافي
def get_dr_response(text):
    text = text.lower()
    if "اهل" in text or "بيت" in text:
        return "الأهل هما السند بس ساعات بيبقوا هما الحمل.. احكي لي بالظبط إيه اللي بيحصل في البيت ومخليك مش طايق الوضع؟ أنا معاك."
    elif "حادث" in text or "خبط" in text:
        return "ألف سلامة عليك! دي خضة وحشة أوي.. ارتاح دلوقتي وطمن جسمك إنك بقيت في أمان. احكي لي حسيت بإيه وقتها؟"
    elif "فشل" in text or "خسر" in text:
        return "مفيش حد بيوصل للقمة من غير ما يقع في حفر كتير. أنت بطل إنك لسه واقف وبتحكي. إيه اللي ناوي تعمله المرة الجاية؟"
    else:
        return "كلامك لمس قلبي.. أنا حاسس بكل كلمة. كمل يا صديقي، الفضفضة هي أول طريق الشفاء. أنا مركز معاك."

if submit and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = get_dr_response(user_input)
    st.session_state.messages.append({"role": "dr", "content": response})
    st.rerun()

# الأزرار التفاعلية (المحفزات)
st.markdown("---")
st.write("### محتاج مساعدة سريعة؟")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✨ شجعني"):
        st.info("أنت قوي جداً لمجرد إنك واجهت مشاعرك النهاردة وجيت هنا. كمل يا بطل!")
with col2:
    if st.button("💡 نصيحة"):
        st.success("جرب تاخد نفس عميق (شهيق 4 ثواني، كتم 4، زفير 4).. جربها دلوقتي وهتحس بفرق.")
with col3:
    if st.button("🗑️ مسح الشات"):
        st.session_state.messages = []
        st.rerun()

# زرار الواتساب (القنبلة)
st.markdown("<br>", unsafe_allow_html=True)
whatsapp_link = "https://wa.me/201009469831"
st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button class="stButton whatsapp-btn" style="width:100%; cursor:pointer;">📞 تواصل مع د. شارون شخصياً (واتساب)</button></a>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; opacity: 0.5;'>Safe Space | د. شارون - خصوصية تامة</p>", unsafe_allow_html=True)
