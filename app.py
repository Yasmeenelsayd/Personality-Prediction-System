import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config("Personality Test", layout="wide")

model = joblib.load('knn_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

questions = [
    'You regularly make new friends.',
       'You spend a lot of your free time exploring various random topics that pique your interest.',
       'Seeing other people cry can easily make you feel like you want to cry too.',
       'You often make a backup plan for a backup plan.',
       'You usually stay calm, even under a lot of pressure.',
       'At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know.',
       'You prefer to completely finish one project before starting another.',
       'You are very sentimental.',
       'You like to use organizing tools like schedules and lists.',
       'Even a small mistake can cause you to doubt your overall abilities and knowledge.',
       'You feel comfortable just walking up to someone you find interesting and striking up a conversation.',
       'You are not too interested in discussing various interpretations and analyses of creative works.',
       'You are more inclined to follow your head than your heart.',
       'You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.',
       'You rarely worry about whether you make a good impression on people you meet.',
       'You enjoy participating in group activities.',
       'You like books and movies that make you come up with your own interpretation of the ending.',
       'Your happiness comes more from helping others accomplish things than your own accomplishments.',
       'You are interested in so many things that you find it difficult to choose what to try next.',
       'You are prone to worrying that things will take a turn for the worse.',
       'You avoid leadership roles in group settings.',
       'You are definitely not an artistic type of person.',
       'You think the world would be a better place if people relied more on rationality and less on their feelings.',
       'You prefer to do your chores before allowing yourself to relax.',
       'You enjoy watching people argue.',
       'You tend to avoid drawing attention to yourself.',
       'Your mood can change very quickly.',
       'You lose patience with people who are not as efficient as you.',
       'You often end up doing things at the last possible moment.',
       'You have always been fascinated by the question of what, if anything, happens after death.',
       'You usually prefer to be around others rather than on your own.',
       'You become bored or lose interest when the discussion gets highly theoretical.',
       'You find it easy to empathize with a person whose experiences are very different from yours.',
       'You usually postpone finalizing decisions for as long as possible.',
       'You rarely second-guess the choices that you have made.',
       'After a long and exhausting week, a lively social event is just what you need.',
       'You enjoy going to art museums.',
       'You often have a hard time understanding other people feelings.',
       'You like to have a to-do list for each day.',
       'You rarely feel insecure.', 'You avoid making phone calls.',
       'You often spend a lot of time trying to understand views that are very different from your own.',
       'In your social circle, you are often the one who contacts your friends and initiates activities.',
       'If your plans are interrupted, your top priority is to get back on track as soon as possible.',
       'You are still bothered by mistakes that you made a long time ago.',
       'You rarely contemplate the reasons for human existence or the meaning of life.',
       'Your emotions control you more than you control them.',
       'You take great care not to make people look bad, even when it is completely their fault.',
       'Your personal work style is closer to spontaneous bursts of energy than organized and consistent efforts.',
       'When someone thinks highly of you, you wonder how long it will take them to feel disappointed in you.',
       'You would love a job that requires you to work alone most of the time.',
       'You believe that pondering abstract philosophical questions is a waste of time.',
       'You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.',
       'You know at first glance how someone is feeling.',
       'You often feel overwhelmed.',
       'You complete things methodically without skipping over any steps.',
       'You are very intrigued by things labeled as controversial.',
       'You would pass along a good opportunity if you thought someone else needed it more.',
       'You struggle with deadlines.',
       'You feel confident that things will work out for you.'
]


response_scale = {
    "Fully Agree": 3,
    "Partially Agree": 2,
    "Slightly Agree": 1,
    "Neutral": 0,
    "Slightly Disagree": -1,
    "Partially Disagree": -2,
    "Fully Disagree": -3
}

if 'responses' not in st.session_state:
    st.session_state.responses = [None] * len(questions)
if 'current_page' not in st.session_state:
    st.session_state.current_page = 0

st.title("Personality Assessment")
st.write("Please answer all 60 questions")
progress = st.progress(sum(1 for r in st.session_state.responses if r is not None) / len(questions))

QUESTIONS_PER_PAGE = 6
total_pages = 10
current_page = st.session_state.current_page
start_idx = current_page * QUESTIONS_PER_PAGE
end_idx = min(start_idx + QUESTIONS_PER_PAGE, len(questions))

st.subheader(f"Step {current_page + 1} of {total_pages} (Questions {start_idx + 1}-{end_idx})")

for i in range(start_idx, end_idx):
    st.subheader(f"**{i + 1}. {questions[i]}**")
    
    cols = st.columns(7)
    for j, (response_text, value) in enumerate(response_scale.items()):
        with cols[j]:
            is_selected = st.session_state.responses[i] == value
            button_label = f"✓ {response_text}" if is_selected else response_text
            button_type = "primary" if is_selected else "secondary"
            
            if st.button(button_label, key=f"btn_{i}_{j}", use_container_width=True, type=button_type):
                st.session_state.responses[i] = value
                st.rerun()
    
    
    st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("Previous Page"):
        if st.session_state.current_page > 0:
            st.session_state.current_page -= 1
            st.rerun()

with col2:
    answered_count = sum(1 for r in st.session_state.responses if r is not None)
    st.write(f"**Progress: {answered_count}/{len(questions)} questions answered**")

with col3:
    if st.button("Next Page"):
        if st.session_state.current_page < total_pages - 1:
            st.session_state.current_page += 1
            st.rerun()


LETTER_MEANINGS = {
    'E': {
        'dimension': 'Extraversion',
        'description': 'Outgoing, energetic, and sociable',
        'full_name': 'Extraversion vs Introversion',
        'E_meaning': 'Extraversion: Draw energy from social interaction',
        'I_meaning': 'Introversion: Recharge through alone time'
    },
    'I': {
        'dimension': 'Introversion',
        'description': 'Reserved, reflective, and independent',
        'full_name': 'Extraversion vs Introversion',
        'E_meaning': 'Extraversion: Draw energy from social interaction',
        'I_meaning': 'Introversion: Recharge through alone time'
    },
    'S': {
        'dimension': 'Sensing',
        'description': 'Practical, factual, and detail-oriented',
        'full_name': 'Sensing vs Intuition',
        'S_meaning': 'Sensing: Focus on concrete facts and details',
        'N_meaning': 'Intuition: Focus on patterns and possibilities'
    },
    'N': {
        'dimension': 'Intuition',
        'description': 'Imaginative, conceptual, and future-focused',
        'full_name': 'Sensing vs Intuition',
        'S_meaning': 'Sensing: Focus on concrete facts and details',
        'N_meaning': 'Intuition: Focus on patterns and possibilities'
    },
    'T': {
        'dimension': 'Thinking',
        'description': 'Logical, objective, and analytical',
        'full_name': 'Thinking vs Feeling',
        'T_meaning': 'Thinking: Decisions based on logic and objectivity',
        'F_meaning': 'Feeling: Decisions based on values and harmony'
    },
    'F': {
        'dimension': 'Feeling',
        'description': 'Empathetic, compassionate, and value-driven',
        'full_name': 'Thinking vs Feeling',
        'T_meaning': 'Thinking: Decisions based on logic and objectivity',
        'F_meaning': 'Feeling: Decisions based on values and harmony'
    },
    'J': {
        'dimension': 'Judging',
        'description': 'Organized, decisive, and planned',
        'full_name': 'Judging vs Perceiving',
        'J_meaning': 'Judging: Prefer structure and closure',
        'P_meaning': 'Perceiving: Prefer flexibility and spontaneity'
    },
    'P': {
        'dimension': 'Perceiving',
        'description': 'Flexible, adaptable, and spontaneous',
        'full_name': 'Judging vs Perceiving',
        'J_meaning': 'Judging: Prefer structure and closure',
        'P_meaning': 'Perceiving: Prefer flexibility and spontaneity'
    }
}

def display_personality_breakdown(personality_type):
    st.subheader("🔍 Understanding Your Personality Type")
    st.write(f"**Your type: {personality_type}**")
    
    cols = st.columns(4)
    for i, letter in enumerate(personality_type):
        with cols[i]:
            info = LETTER_MEANINGS[letter]
            st.markdown(f"""
            <div style='text-align: center; padding: 15px; border-radius: 10px; background-color: #f0f2f6;'>
                <h3 style='color: #ff4b4b; margin: 0;'>{letter}</h3>
                <p style='font-weight: bold; margin: 5px 0;'>{info['dimension']}</p>
                <p style='font-size: 0.9em; margin: 0;'>{info['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.subheader("📖 Detailed Breakdown")
    
    dimensions = [
        ('Extraversion vs Introversion', personality_type[0], 'EI'),
        ('Sensing vs Intuition', personality_type[1], 'SN'),
        ('Thinking vs Feeling', personality_type[2], 'TF'),
        ('Judging vs Perceiving', personality_type[3], 'JP')
    ]
    
    for dim_name, user_letter, pair in dimensions:
        st.write(f"**{dim_name}**")

        letter1, letter2 = pair[0], pair[1]
        user_info = LETTER_MEANINGS[user_letter]
        other_letter = letter2 if user_letter == letter1 else letter1
        
        col1, col2 = st.columns(2)
        with col1:
            if user_letter == letter1:
                st.success(f"**{letter1} - {LETTER_MEANINGS[letter1]['dimension']}** ✅")
                st.write(f"*{user_info[f'{user_letter}_meaning']}*")
            else:
                st.info(f"**{letter1} - {LETTER_MEANINGS[letter1]['dimension']}**")
                st.write(f"*{LETTER_MEANINGS[letter1][f'{letter1}_meaning']}*")
        
        with col2:
            if user_letter == letter2:
                st.success(f"**{letter2} - {LETTER_MEANINGS[letter2]['dimension']}** ✅")
                st.write(f"*{user_info[f'{user_letter}_meaning']}*")
            else:
                st.info(f"**{letter2} - {LETTER_MEANINGS[letter2]['dimension']}**")
                st.write(f"*{LETTER_MEANINGS[letter2][f'{letter2}_meaning']}*")
        
        st.write("---")


if None not in st.session_state.responses:
    st.success("All questions completed!")
    
    if st.button("View Results and Prediction"):
        responses_array = np.array(st.session_state.responses).reshape(1, -1)
        prediction = model.predict(responses_array)
        prediction_name = label_encoder.inverse_transform(prediction)
        personality_type = prediction_name[0]
        st.subheader(f"Your predicted personality type is: **{personality_type}**")

        display_personality_breakdown(personality_type)

        st.subheader("🌟 Notable Characteristics")
        TYPE_CHARACTERISTICS = {
            'INTJ': ['Strategic', 'Independent', 'Analytical', 'Future-oriented'],
            'INTP': ['Innovative', 'Theoretical', 'Logical', 'Curious'],
            'ENTJ': ['Commanding', 'Strategic', 'Efficient', 'Decisive'],
            'ENTP': ['Inventive', 'Energetic', 'Debative', 'Resourceful'],
            'INFJ': ['Insightful', 'Compassionate', 'Visionary', 'Determined'],
            'INFP': ['Idealistic', 'Empathetic', 'Creative', 'Authentic'],
            'ENFJ': ['Inspirational', 'Empathetic', 'Persuasive', 'Organized'],
            'ENFP': ['Enthusiastic', 'Creative', 'Sociable', 'Spontaneous'],
            'ISTJ': ['Responsible', 'Practical', 'Organized', 'Detail-oriented'],
            'ISFJ': ['Supportive', 'Reliable', 'Caring', 'Thorough'],
            'ESTJ': ['Efficient', 'Organized', 'Direct', 'Traditional'],
            'ESFJ': ['Sociable', 'Caring', 'Popular', 'Cooperative'],
            'ISTP': ['Practical', 'Analytical', 'Adaptable', 'Risk-taking'],
            'ISFP': ['Artistic', 'Gentle', 'Flexible', 'Present-focused'],
            'ESTP': ['Energetic', 'Practical', 'Persuasive', 'Spontaneous'],
            'ESFP': ['Playful', 'Sociable', 'Spontaneous', 'Generous']
        }
        
        if personality_type in TYPE_CHARACTERISTICS:
            st.write("**Common traits:**")
            for trait in TYPE_CHARACTERISTICS[personality_type]:
                st.write(f"• {trait}")


if st.button("Reset Assessment"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
    
    
