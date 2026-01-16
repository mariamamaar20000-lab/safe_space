import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Safe Space AI | Dr. Sharon", page_icon="🧠", layout="centered")

# التصميم الكحلي الفخم (CSS)
st.markdown("""
    <style>
    .stApp {
        background-color: #1a2634; /* لون كحلي غامق */
        color: white;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #2c3e50 !important;
        color: white !important;
        border: 1px solid #3498db !important;
    }
    h1, h2, h3, p {
        color: white !important;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 20px;
        width: 100%;
        border: none;
    }
    .bot-msg {
        background-color: #2c3e50;
        padding: 15px;
        border-radius: 15px;
        border-right: 5px solid #3498db;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 عيادة الذكاء الاصطناعي | د. شارون")
st.write("مرحباً بك في مساحتك الخاصة. أنا هنا لأسمعك وأحلل مشكلاتك بكل سرية.")

# منطقة الدردشة
user_problem = st.text_area("صف لي ما تشعر به أو المشكلة التي تواجهك:")

if st.button("تحليل المشكلة والحصول على حل"):
    if user_problem:
        with st.spinner('جاري تحليل كلماتك بعمق...'):
            time.sleep(2) # محاكاة تفكير الذكاء الاصطناعي
            
            st.subheader("💡 تحليل العيادة الذكية:")
            
            # منطق رد تفاعلي (Simulated AI Logic)
            if "حزين" in user_problem or "ضيق" in user_problem:
                response = "أشعر بحزنك يا صديقي. تذكر أن الغيوم لا تبقى للأبد، والتنفس بعمق الآن هو أول خطوة للهدوء. هل جربت كتابة ما يزعجك في ورقة وحرقها؟"
            elif "قلق" in user_problem or "خايف" in user_problem:
                response = "القلق هو مجرد إنذار خاطئ من العقل. أنت في أمان الآن. حاول تركيز نظرك على 3 أشياء زرقاء حولك الآن لتهدئة جهازك العصبي."
            elif "تعبان" in user_problem or "مرهق" in user_problem:
                response = "جسدك يطلب منك الهدنة. أنت لست في سباق مع أحد. خذ قسطاً من الراحة، فالعالم لن يتوقف إذا ارتحت قليلاً."
            else:
                response = "شكرًا لثقتك ومشاركتي هذه المشاعر. أنت شخص شجاع جداً لمجرد حديثك عن هذا. ابدأ بالتركيز على ما يمكنك التحكم فيه فقط اليوم."
            
            st.markdown(f'<div class="bot-msg">{response}</div>', unsafe_allow_html=True)
            st.balloons()
    else:
        st.warning("من فضلك اكتب شيئاً أولاً لأتمكن من مساعدتك.")

# إضافة نصيحة جانبية
st.sidebar.title("إحصائيات الجلسة")
st.sidebar.info("الذكاء الاصطناعي نشط الآن وجاهز للاستماع.")
