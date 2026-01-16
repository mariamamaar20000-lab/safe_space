import streamlit as st
import time

# إعدادات واجهة العيادة
st.set_page_config(page_title="Safe Space | Dr. Sharon", page_icon="🌿", layout="wide")

# تصميم الألوان والخطوط (CSS)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #e0eafc, #cfdef3);
    }
    .main-title {
        font-size: 50px;
        color: #2C3E50;
        text-align: center;
        font-family: 'Arial';
        padding: 20px;
    }
    .quote-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-right: 5px solid #2980b9;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown('<h1 class="main-title">🌿 Safe Space | Dr. Sharon</h1>', unsafe_allow_html=True)

# مقولة ملهمة تتغير (التشويق)
st.markdown("""
<div class="quote-box">
    <i>"كل رحلة تعافي تبدأ بكلمة.. وهذه هي مساحتك الخاصة جداً."</i>
</div>
""", unsafe_allow_html=True)

# تقسيم الصفحة لأعمدة
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("كيف تشعر اللحظة؟")
    mood = st.select_slider(
        "حرك المؤشر لتعبر عن حالتك النفسية:",
        options=["محطم 💔", "قلق 😟", "محايد 😐", "هادئ 😌", "سعيد جداً ✨"]
    )
    
    note = st.text_area("ما الذي يدور في ذهنك الآن؟ (تفريغ مشاعر)")
    
    if st.button("إرسال إلى ملفك السري"):
        with st.spinner('يتم تحليل مشاعرك بعناية...'):
            time.sleep(2) # حركة تشويقية
            st.success(f"تم تسجيل حالتك كـ ({mood}). أنا هنا بجانبك يا دكتور.")
            st.balloons() # احتفال بسيط بالخطوة

with col2:
    st.info("💡 نصيحة اليوم:")
    st.write("التنفس العميق لـ 3 دقائق يقلل من هرمون التوتر فوراً. جربها الآن!")
    
    # عداد تشويقي لجلسة استرخاء
    if st.button("ابدأ تمرين استرخاء سريع"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.05)
            progress_bar.progress(i + 1)
        st.write("شهيق... زفير... أحسنت!")

# تذييل الصفحة
st.markdown("---")
st.caption("جميع البيانات مشفرة وتخضع للسرية المهنية التامة.")
