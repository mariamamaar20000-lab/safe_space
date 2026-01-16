import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Safe Space | Dr. Sharon", page_icon="🌿", layout="centered")

# التصميم الكحلي الفخم اللي طلبته
st.markdown("""
    <style>
    .stApp { background-color: #0b1120; color: #e2e8f0; }
    .main-title { font-size: 38px; color: #38bdf8; text-align: center; font-weight: bold; padding: 20px; }
    .stTextArea textarea { background-color: #1e293b !important; color: white !important; border: 1px solid #38bdf8 !important; border-radius: 15px !important; }
    .stButton>button { background: linear-gradient(90deg, #0ea5e9, #6366f1); color: white; border-radius: 12px; font-weight: bold; border: none; padding: 10px; width: 100%; }
    .chat-bubble { background-color: #1e293b; padding: 25px; border-radius: 20px; border-right: 6px solid #38bdf8; margin-top: 20px; font-size: 19px; line-height: 1.7; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">🌿 Safe Space | Dr. Sharon</div>', unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 18px;'>أنا دكتور شارون.. احكي لي أي حاجة حصلت معاك، أنا هنا عشان أسمعك وأفهمك بجد. ❤️</p>", unsafe_allow_html=True)

# خانة إدخال المشكلة
user_input = st.text_area("", placeholder="فضفض هنا.. مهما كان اللي حصل، أنا معاك..", height=150)

# محرك الردود الذكي والمجاني (بلهجة مصرية حكيمة)
def get_pro_response(text):
    text = text.strip().lower()
    
    # ردود ذكية شاملة لأي موقف (حادثة، فشل، ضيق، مشاكل أهل)
    if any(word in text for word in ["حادث", "وجع", "مستشفى", "خبط"]):
        return "ألف سلامة على قلبك! دي خضة كبيرة أوي ومقدر جداً إنك لسه تحت تأثير الصدمة. أهم حاجة إنك وسطنا دلوقتي وبخير. احكي لي، جسمك وجعك؟ ولا الخضة هي اللي مأثرة أكتر؟ أنا جنبك متقلقش. 🤕💙"
    
    if any(word in text for word in ["فشل", "سقط", "خسر", "رفض"]):
        return "بص لي هنا.. الفشل ده مجرد 'محطة' مش نهاية الطريق. مفيش حد نجح إلا لما وقع مية مرة. أنت بطل إنك لسه بتحاول وبتحكي. قولي إيه اللي حاسس إنه عطلك؟ ونفكر سوا نصلحه إزاي المرة الجاية. ✨💪"
    
    if any(word in text for word in ["أهل", "بابا", "ماما", "البيت", "زهقت"]):
        return "الأهل هما أصعب علاقة في الدنيا، حب كبير بس ساعات بيبقى فيه ضغط مبيتحملش. ما تزهقش منهم، هم ساعات مبيفهموش لغتنا. احكي لي طيب، إيه أكتر موقف النهاردة ضايقك معاهم؟ نطلع اللي جوانا عشان نرتاح. 🏠🫂"

    if any(word in text for word in ["وحد", "لوحدي", "محدش", "حزين"]):
        return "إحساس الوحدة ده غدار، بيحسسنا إننا في جزيرة مهجورة.. بس أنا معاك دلوقتي وسامعك. أنت شخص غالي وليك قيمة كبيرة حتى لو اللي حوليك مش شايفين ده دلوقتي. قولي، إيه اللي مخليك حاسس إنك لوحدك؟ 🌊🤝"

    if len(text) > 10:
        return "كلامك فيه تفاصيل كتير ومهمة جداً.. أنا حاسس بكل حرف كتبته. واضح إنك شايل كتير في قلبك والوقت جه إنك ترتاح. كمل حكايتك، أنا كدكتور شارون مركز معاك وعايز أساعدك نعدي الأزمة دي سوا. 😊🌿"
    
    return "أنا معاك وسامعك.. كمل فضفضة، قولي إيه اللي حصل بالظبط ومضايقك؟ أنا هنا عشانك. ❤️"

if st.button("تحدث مع د. شارون (جلسة خاصة)"):
    if user_input:
        with st.spinner('دكتور شارون بيفكر في كلامك بعناية...'):
            time.sleep(2)
            response = get_pro_response(user_input)
            st.markdown(f'<div class="chat-bubble"><b>د. شارون:</b><br>{response}</div>', unsafe_allow_html=True)
            if "فشل" in user_input or "خسرت" in user_input:
                st.snow()
    else:
        st.info("يا بطل، اكتب أي حاجة شاغلة بالك عشان أقدر أرد عليك! 😊")

st.markdown("<br><hr><p style='text-align: center; opacity: 0.5;'>جلسة سرية تماماً - دكتور شارون المصري</p>", unsafe_allow_html=True)
