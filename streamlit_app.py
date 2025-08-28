import streamlit as st
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Sai Sushanth Varma Kalidindi",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .open-to-work {
        background-color: #28a745;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        text-align: center;
        font-weight: bold;
        margin: 1rem 0;
    }
    .section-header {
        color: #1f77b4;
        font-size: 1.8rem;
        font-weight: 600;
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
    }
    .skill-tag {
        background-color: #f0f2f6;
        color: #262730;
        padding: 0.25rem 0.5rem;
        margin: 0.25rem;
        border-radius: 15px;
        font-size: 0.85rem;
        display: inline-block;
    }
    .contact-info {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
    
    [data-testid="stTabs"] button {
        font-size: 1.5rem !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Top navigation
def top_navigation():
    # Navigation tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Home", "About", "Research", "Publications", "Experience", "Skills", "Contact"
    ])
    
    with tab1:
        show_home()
    with tab2:
        show_about()
    with tab3:
        show_research()
    with tab4:
        show_publications()
    with tab5:
        show_experience()
    with tab6:
        show_skills()
    with tab7:
        show_contact()

# Home Page
def show_home():
    # Header with photo placeholder
    #col1, col2, col3 = st.columns([1, 2, 1])
    #with col2:
    #    st.markdown('<h1 class="main-header">Sai Sushanth Varma Kalidindi</h1>', unsafe_allow_html=True)
    #    st.markdown("### AI Research Developer | Industrial PhD Candidate")
    

    # Header with photo on the right
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<h1 class="main-header">Sai Sushanth Varma Kalidindi</h1>', unsafe_allow_html=True)
        st.markdown("### AI Research Developer | Industrial PhD Candidate")
    with col2:
        st.image("profile.jpg", width=150)  # Replace with your image file path or URL

    
    # Brief overview
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Welcome to My Portfolio
        
        I am a AI Research Developer with 5+ years of experience developing AI solutions 
        for energy and medical applications. Currently concluding an Industrial PhD centered on 
        developing and integrating deep learning ML models for residential buildings for District Heating Energy Optimization .
        
        **Current Focus:**
        - Machine Learning & Deep Learning & Reinforcement Learning
        - Context-aware Transformer Models for Temperature Prediction
        - District Heating Optimization using AI
        
        **Looking for opportunities in:**
        - Machine Learning positions
        - AI/ML Engineering roles
        - Data Science roles
        """)
    
    with col2:
        st.markdown("""
        ### Quick Stats
        - **5+** Years Experience in AI/ML
        - **Multiple** Publications in AI/ML
        - Developed and Deployed AI models across **148+** buildings 
        
        ### Strong areas
        - Machine Learning
        - Deep Learning
        - Reinforcement Learning
        - Computer Vision
        - Natural Language Processing
        - Building Energy Systems
        """)
    
    # Recent highlights
    st.markdown("---")
    st.markdown("## Recent Highlights")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Latest Research:** Adaptive Context Embedding for Temperature Prediction (ECAI 2024)")
    
    with col2:
        st.success("**Achievement:** Up to 20% energy savings in district heating systems in and around stockholm")
    
    with col3:
        st.warning("**Current:** Completing Industrial PhD at Örebro University")

# About Page
def show_about():
    st.markdown('<h1 class="section-header">About Me</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Professional Summary
        
        I am a dedicated Machine Learning specialist with a unique blend of academic rigor and 
        industry experience. My research focuses on applying cutting-edge AI techniques to solve 
        real-world problems in building energy systems and medical applications.
        
        ### Current Position
        **AI Research Developer** at EcoGuard AB, Sweden (May 2021 - Present)
        - Developing context-aware transformer models for indoor temperature prediction
        - Implementing hybrid deep learning-reinforcement learning architectures
        - Achieving up to 20% energy savings in district heating optimization
        
        ### Education Journey
        
        **Industrial PhD in Artificial Intelligence** - Örebro University (2021-2025)
        - Research Focus: Deep learning and Reinforcement Learning applications for energy optimization
        - Key publications in AAAI, ECAI, and Building and Environment journals
        
        **Master's in Embedded and Intelligent Systems** - Halmstad University (2018-2020)
        - Specialized in AI, robotics, and intelligent systems
        - Thesis: Analyzing white blood cells using deep learning (95% accuracy)
        
        **Bachelor's in Electronics and Communications** - GITAM University (2014-2018)
        - Foundation in digital electronics, communications, and programming
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Skills
        - Machine Learning
        - Deep Learning
        - Reinforcement Learning
        - Computer Vision
        - Natural Language Processing
        - Building Energy Systems
        - Medical AI Applications
        
        ### 🌍 Languages
        - **English:** Professional
        - **Swedish:** Beginner
        
        ### 🏆 Key Achievements
        - 40% reduction in temperature prediction error
        - 20% energy savings in heating systems
        - 148+ buildings analyzed across Sweden & Finland
        - Multiple peer-reviewed publications
        
        ### 🎨 Interests
        - Badminton
        - Building RC cars
        - IoT Projects
        - Cooking
        """)

# Research Page
def show_research():
    st.markdown('<h1 class="section-header">Research Areas</h1>', unsafe_allow_html=True)
    
    # Main research areas
    research_areas = [
        {
            "title": "🏠 Building Energy Systems",
            "description": "Developing AI solutions for optimizing energy consumption in residential buildings using district heating systems.",
            "key_work": [
                "Context-aware transformer models for temperature prediction",
                "Hybrid deep learning-reinforcement learning architectures",
                "Analysis of 148+ buildings across Sweden and Finland",
                "Up to 20% energy savings achieved"
            ]
        },
        {
            "title": "🤖 Deep Learning & Transformers", 
            "description": "Advancing transformer architectures for time series prediction and contextual understanding.",
            "key_work": [
                "Adaptive context embedding for residential buildings",
                "Multi-head attention mechanisms for sensor data",
                "Temporal positional encoding for time series",
                "Building-specific thermal behavior modeling"
            ]
        },
        {
            "title": "🎮 Reinforcement Learning",
            "description": "Applying RL techniques for real-time control and optimization of complex systems.",
            "key_work": [
                "Deep Q-Network (DQN) control systems",
                "Safety-constrained RL for heating systems", 
                "Multi-objective optimization (comfort + efficiency)",
                "Real-time heat distribution management"
            ]
        },
        {
            "title": "🩺 Medical AI Applications",
            "description": "Leveraging computer vision and deep learning for medical image analysis and diagnostics.",
            "key_work": [
                "White blood cell analysis (95% accuracy)",
                "CNN-LSTM architectures for medical imaging",
                "Segmentation models for cell detection",
                "Deep learning for diagnostic applications"
            ]
        }
    ]
    
    for area in research_areas:
        with st.expander(area["title"]):
            st.write(area["description"])
            st.write("**Key Contributions:**")
            for work in area["key_work"]:
                st.write(f"• {work}")
    
    # Current projects
    st.markdown("---")
    st.markdown("## 🔬 Current Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### District Heating Optimization with multi-agent approach
        **Status:** Active Work in Progress/Research (2024-2025)
        
        Developing an integrated framework combining adaptive context-aware transformers 
        with deep reinforcement learning for district heating control in residential buildings.
        
        **Key Innovations:**
        - Building-specific contextual embeddings with LLMs
        - Multi-objective reward functions for Reinforcement learning agents
        - Safety-constrained control policies
        - Real-world deployment in Stockholm and Helsinki
        """)
    
    with col2:
        st.markdown("""
        ### Context-Aware AI Models
        **Status:** Published (ECAI 2024)
        
        Created novel transformer architectures that adapt to building-specific characteristics
        for improved temperature prediction accuracy.
        
        **Achievements:**
        - 40% reduction in prediction error
        - Generalization across diverse building types
        - Integration of geographical and structural features
        - Real-time operational deployment
        """)

# Publications Page
def show_publications():
    st.markdown('<h1 class="section-header">Publications</h1>', unsafe_allow_html=True)
    
    publications = [
        {
            "title": "District Heating Optimization in Residential Buildings Using Reinforcement Learning with Adaptive Context-aware Predictive Environment",
            "authors": "Sai Sushanth Varma Kalidindi, Hadi Banaee, Hans Karlsson, Amy Loutfi",
            "venue": "Submitted to Elsevier (2025)",
            "type": "Journal Article",
            "status": "Under Review",
            "abstract": "This work presents an integrated framework combining adaptive context-aware transformer model as environment for deep reinforcement learning agents for district heating optimization. Using real-world data from 148 residential buildings, we achieved significant energy savings of 7.40% to 14.85% while maintaining indoor temperatures within ±0.5°C of desired setpoints.",
            "github": "https://github.com/SaiSushanthVarma/energy-Optimization-RL-Transformer-",  # Update with actual links
            "pdf": "https://github.com/SaiSushanthVarma/energy-Optimization-RL-Transformer-/blob/main/RL%2BTransformer.pdf"
        },
        {
            "title": "Adaptive Context Embedding for Temperature Prediction in Residential Buildings",
            "authors": "Sai Sushanth Varma Kalidindi, Hadi Banaee, Hans Karlsson, Amy Loutfi",
            "venue": "ECAI 2024, IOS Press",
            "type": "Conference Paper",
            "status": "Published",
            "abstract": "This paper presents a novel transformer-based model that adapts contextual meta-data of residential buildings for enhanced temperature prediction. The model integrates temporal data with adaptive embedding achieving RMSE values between 0.18–0.24 °C for Swedish buildings.",
            "github": "https://github.com/SaiSushanthVarma/Adaptive-context-embedding-Transformer",
            "pdf": "https://github.com/SaiSushanthVarma/Adaptive-context-embedding-Transformer/blob/main/Adaptive_context_aware_transformer.pdf"
        },
        {
            "title": "Transformers and Contextual Information in Temperature Prediction of Residential Buildings for Improved Energy Consumption",
            "authors": "Sai Sushanth Varma Kalidindi, Hadi Banaee, Amy Loutfi", 
            "venue": "AAAI 2022 Workshop",
            "type": "Workshop Paper",
            "status": "Published",
            "abstract": "We present a prediction model utilizing transformer architectures for indoor temperature prediction in residential buildings. The study demonstrates 80% improvement in prediction accuracy using transformer models over LSTM.",
            "github": "https://github.com/SaiSushanthVarma/Identifying-Context-data",
            "pdf": "https://github.com/SaiSushanthVarma/Identifying-Context-data/blob/main/Identfying_context.pdf"
        },
        {
            "title": "Indoor temperature prediction with context-aware models in residential buildings",
            "authors": "Sai Sushanth Varma Kalidindi, Hadi Banaee, Hans Karlsson, Amy Loutfi",
            "venue": "Building and Environment, Elsevier",
            "type": "Journal Article", 
            "status": "Published",
            "abstract": "This paper presents a novel approach for predicting average indoor temperature in residential buildings, utilizing contextual factors. The transformer-based models show improvements in R² of 4%–27% in a 6 h prediction horizon.",
            "github": "https://github.com/SaiSushanthVarma/Time-series-prediction-with-context-aware-models",
            "pdf": "https://github.com/SaiSushanthVarma/Time-series-prediction-with-context-aware-models/blob/main/Context_aware_transformer.pdf"
        }
    ]
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_type = st.selectbox("Filter by Type:", ["All", "Journal Article", "Conference Paper", "Workshop Paper"])
    with col2:
        filter_status = st.selectbox("Filter by Status:", ["All", "Published", "Under Review"])
    with col3:
        sort_by = st.selectbox("Sort by:", ["Recent First", "Alphabetical"])
    
    # Filter publications
    filtered_pubs = publications
    if filter_type != "All":
        filtered_pubs = [p for p in filtered_pubs if p["type"] == filter_type]
    if filter_status != "All":
        filtered_pubs = [p for p in filtered_pubs if p["status"] == filter_status]
    
    # Display publications
    for pub in filtered_pubs:
        with st.expander(f"📄 {pub['title']}", expanded=False):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.write(f"**Authors:** {pub['authors']}")
                st.write(f"**Venue:** {pub['venue']}")
                st.write(f"**Abstract:** {pub['abstract']}")
            
            with col2:
                st.write(f"**Type:** {pub['type']}")
                st.write(f"**Status:** {pub['status']}")
                
                # Action buttons
                if pub['github']:
                    st.markdown(f"[📱 GitHub]({pub['github']})")
                if pub['pdf']:
                    st.markdown(f"[📄 PDF]({pub['pdf']})")
    
    # Publication statistics
    st.markdown("---")
    st.markdown("## 📊 Publication Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Publications", len(publications))
    with col2:
        st.metric("Journal Articles", len([p for p in publications if p['type'] == 'Journal Article']))
    with col3:
        st.metric("Conference Papers", len([p for p in publications if p['type'] == 'Conference Paper']))
    with col4:
        st.metric("Under Review", len([p for p in publications if p['status'] == 'Under Review']))

# Experience Page
def show_experience():
    st.markdown('<h1 class="section-header">Professional Experience</h1>', unsafe_allow_html=True)
    
    experiences = [
        {
            "title": "AI Research Developer",
            "company": "EcoGuard AB",
            "location": "Örebro, Sweden",
            "period": "May 2021 - Present",
            "description": [
                "Developed context-aware transformer models for indoor temperature prediction in residential buildings, reducing prediction error by 40%",
                "Implemented hybrid deep learning-reinforcement learning architecture for district heating optimization, achieving up to 20% energy savings",
                "Designed adaptive context embedding system for building-specific thermal modelling across 148+ buildings in Sweden and Finland", 
                "Created Deep Q-Network (DQN) control system with safety constraints for real-time heat distribution management",
                "Led big data analysis and classification of 40,000+ residential buildings to optimize energy consumption patterns"
            ],
            "skills": ["Machine Learning", "Reinforcement Learning", "Transformer Models", "LSTM", "Random Forest", "XGBoost", "Python", "TensorFlow", "PyTorch", "Time-series Analysis", "Git", "InfluxDB", "MongoDB", "Pytorch", "Tensorflow", "AWS"]
        },
        {
            "title": "Machine Learning Engineer",
            "company": "Inovotech Consulting",
            "location": "Gothenburg, Sweden", 
            "period": "Dec 2020 - Apr 2021",
            "description": [
                "Developed a web scraping algorithm with selenium and ML to provide job classifications to the HR team",
                "Data extraction and analysis using deep-learning methods (OCR, NER, TensorFlow)",
                "Built automated data processing pipelines for recruitment analytics"
            ],
            "skills": ["Machine Learning", "Web Scraping", "OCR", "NER", "Selenium", "Data Analysis"]
        },
        {
            "title": "Master Thesis Student",
            "company": "Hemocue AB",
            "location": "Angelholm, Sweden",
            "period": "Nov 2019 - Oct 2020", 
            "description": [
                "Analyzed white blood cells in blood samples using deep-learning techniques",
                "Achieved higher accuracy (95%) in detecting cells using novel approaches (CNN-LSTM, Segmentation models)",
                "Developed computer vision solutions for medical diagnostics"
            ],
            "skills": ["Computer Vision", "CNN", "LSTM", "Medical AI", "Image Segmentation"]
        },
        {
            "title": "Software Development Engineer",
            "company": "Varaha Racing",
            "location": "Visakhapatnam, India",
            "period": "Jul 2017 - Jul 2018",
            "description": [
                "Coordinated with CAN bus systems to evaluate and improve software and hardware interfaces for an electric ATV",
                "Created electrical schematics using AutoCAD Electrical software",
                "Developed embedded systems for automotive applications"
            ],
            "skills": ["Embedded Systems", "CAN Bus", "AutoCAD", "Hardware Design"]
        }
    ]
    
    for i, exp in enumerate(experiences):
        with st.container():
            st.markdown(f"### {exp['title']} @ {exp['company']}")
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.write(f"📍 {exp['location']} | 📅 {exp['period']}")
                
                for desc in exp['description']:
                    st.write(f"• {desc}")
            
            with col2:
                st.write("**Key Skills:**")
                for skill in exp['skills']:
                    st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
        
        if i < len(experiences) - 1:
            st.markdown("---")

# Skills Page  
def show_skills():
    st.markdown('<h1 class="section-header">Technical Skills</h1>', unsafe_allow_html=True)
    
    skills_data = {
        "Machine Learning & AI": {
            "skills": ["Machine Learning", "Deep Learning", "Reinforcement Learning", "Computer Vision", "Natural Language Processing", "Transformers", "Neural Networks", "CNN", "LSTM", "GenAI"],
            "proficiency": [95, 95, 90, 85, 80, 95, 90, 90, 90, 80]
        },
        "Programming & Frameworks": {
            "skills": ["Python", "TensorFlow", "PyTorch", "Keras", "SQL", "NoSQL", "Git", "C++", "Java"],
            "proficiency": [95, 90, 85, 85, 80, 75, 90, 70, 70]
        },
        "Data Science & Analysis": {
            "skills": ["Data Analysis", "Data Mining", "Statistical Modelling", "Quantitative Analysis", "Experimental Design", "Scientific Writing"],
            "proficiency": [90, 85, 80, 85, 80, 85]
        },
        "Cloud & Infrastructure": {
            "skills": ["AWS", "GCP", "MLOps", "Docker", "Linux"],
            "proficiency": [75, 70, 80, 75, 80]
        },
        "Domain Expertise": {
            "skills": ["Building Energy Systems", "District Heating", "Medical AI", "Time Series Analysis", "Optimization"],
            "proficiency": [95, 95, 85, 90, 85]
        }
    }
    
    tabs = st.tabs(list(skills_data.keys()))
    
    for i, (category, data) in enumerate(skills_data.items()):
        with tabs[i]:
            st.markdown(f"### {category}")
            
            for j, (skill, prof) in enumerate(zip(data['skills'], data['proficiency'])):
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    st.write(skill)
                with col2:
                    st.progress(prof / 100)
                with col3:
                    st.write(f"{prof}%")
    
    # Certifications & Awards
    st.markdown("---")
    st.markdown("## 🏆 Certifications & Awards")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎓 Academic Achievements
        - **Industrial PhD Candidate** - Örebro University
        - **Master's in Embedded Systems** - Halmstad University  
        - **Publications** in top-tier conferences (ECAI, AAAI)
        - **Research Excellence** in AI applications
        """)
    
    with col2:
        st.markdown("""
        ### 💼 Professional Recognition
        - **AI Research Developer** - EcoGuard AB
        - **40% Improvement** in temperature prediction accuracy
        - **20% Energy Savings** in district heating systems
        - **148+ Buildings** analyzed across multiple countries
        """)

# Contact Page
def show_contact():
    st.markdown('<h1 class="section-header">Contact Information</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h3>📧 Get In Touch</h3>
            <p><strong>Email:</strong> sushanth.kalidindi@gmail.com</p>
            <p><strong>Phone:</strong> +46 79 345 6879</p>
            <p><strong>Location:</strong> Fagersta, Sweden 73747</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Contact form
        st.markdown("### 💬 Send me a message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=120)
            
            if st.form_submit_button("Send Message"):
                if name and email and message:
                    st.success("Thank you for your message! I'll get back to you soon.")
                    # In a real app, you'd integrate with an email service here
                else:
                    st.error("Please fill in all fields.")
    
    with col2:
        st.markdown("""
        ### 🔗 Professional Links
        
        **LinkedIn**  
        [Connect with me](https://www.linkedin.com/in/sushanthkalidindi/)
        
        **GitHub**  
        [View my repositories](https://github.com/SaiSushanthVarma)
        
        **Google Scholar**  
        [Research publications](https://scholar.google.com/citations?hl=en&user=-x9d_xIAAAAJ)
        
        
        ### 🎯 Current Status
        
        **🟢 OPEN TO WORK**
        
        Looking for opportunities in:
        - AI / ML Positions
        - AI Engineering positions
        - Data Science roles  
        
        **Preferred Locations:**
        - Sweden (Stockholm, Västerås, Örebro)
        - Remote opportunities
        
        ### 📅 Availability
        - **Notice Period:** 2 Weeks
        - **Travel:** Available for interviews
        - **Remote Work:** Yes
        - **Relocation:** Open to discussion
        """)
        
        # Quick stats
        st.markdown("---")
        st.markdown("### 📊 Quick Response")
        st.info("I typically respond to emails within 24 hours")
        st.info("Available for calls during CET business hours")

# Main app logic
def main():
    # Open to Work banner at the top
    st.markdown("""
    <div style='background-color: #28a745; color: white; padding: 1rem; 
    border-radius: 10px; text-align: center; margin: 1rem 0;'>
        <strong>🟢 OPEN TO WORK</strong> - AI Research Developer| 
        📧 sushanth.kalidindi@gmail.com | 
        💼 <a href="https://www.linkedin.com/in/sushanthkalidindi/" style="color: white;">LinkedIn</a> | 
        🐙 <a href="https://github.com/SaiSushanthVarma" style="color: white;">GitHub</a>
        📄 <a href="cv.pdf" download style="color: white; font-weight: bold;">Download Resume</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.download_button(
    label="📄 Download CV (PDF)",
    data=open("cv.pdf", "rb"),
    file_name="SaiSushanthVarma_CV.pdf",
    mime="application/pdf"
    )
    # Use the top navigation
    top_navigation()

if __name__ == "__main__":
    main()

