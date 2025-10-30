import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime
import base64

def send_email(name, email, phone, family_members, special_requirements):
    try:
        # Email configuration - you'll need to set these in Streamlit secrets
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        # Try different ways to access secrets
        try:
            sender_email = st.secrets["gmail"]["GMAIL_USER"]
            sender_password = st.secrets["gmail"]["GMAIL_PASSWORD"]
        except:
            try:
                sender_email = st.secrets["GMAIL_USER"]
                sender_password = st.secrets["GMAIL_PASSWORD"]
            except Exception as e:
                print(e)
                # Fallback to environment variables
                sender_email = "emirateskannadigaru@gmail.com"
                sender_password = "sicyfifhuudhbkvl"
                pass
        
        if not sender_email or not sender_password:
            st.warning("⚠️ Email configuration not found. Registration data saved locally.")
            # Save to local file as backup
            with open("registrations.txt", "a", encoding="utf-8") as f:
                f.write(f"\n--- Registration at {datetime.now()} ---\n")
                f.write(f"Name: {name}\nEmail: {email}\nPhone: {phone}\n")
                f.write(f"Family Members: {family_members}\nSpecial Requirements: {special_requirements}\n")
                f.write("-" * 50 + "\n")
            return True
        to_email = sender_email
        if email:
            to_email = email
        # Create message
        cc_emails = [sender_email, 'javabit041@gmail.com']
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email  # Send to yourself
        msg["Cc"] = ", ".join(cc_emails)
        msg['Subject'] = f"Kannada Rajyotsava Registration - {name}"
        
        # Email body
        body = f"""
        New Registration for Kannada Rajyotsava Celebration
        
        Event Details:
        Date: November 15th, 2025
        Time: 10 AM - 4 PM
        Venue: Jabeel Park
        
        Registrant Information:
        Name: {name}
        Email: {email}
        Phone: {phone}
        Number of Family Members: {family_members}
        Special Requirements: {special_requirements if special_requirements else 'None'}
        
        Registration Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, sender_email, text)
        server.quit()
        
        return True
    except Exception as e:
        st.error(f"Failed to send email: {str(e)}")
        return False

def main():
    # Page configuration
    st.set_page_config(
        page_title="Kannada Rajyotsava 2025 - EK Celebration",
        page_icon="🎉",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    hide_streamlit_style = """
        <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .st-emotion-cache-t1wise {
                padding: 0rem 20rem 1rem;
                }
             .st-emotion-cache-b499ls {
            padding: 0rem 5rem 1rem;
                } 
                
                .st-emotion-cache-zy6yx3 {
            padding: 0rem 1rem 1rem;
                } 
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    hide_streamlit_style = """
                    <style>
                    .navbar-toggler {
                        'background-color': '#526d94 !important';
                    }

                    .text-white {
                        'background-color': '#526d94 !important';
                    }
                    .st-emotion-cache-rrm7oe {
                      text-decoration: underline;
                    }

                    </style>
                    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    import warnings
    warnings.filterwarnings("ignore", message=".*use_container_width.*")
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # Custom CSS for beautiful styling
    st.markdown("""
    <style>
    .main {
        padding-top: 0rem;
    }
    
    /* Mobile-Optimized Tabs */
    @media (max-width: 768px) {
        .mobile-nav-container {
            display: block !important;
            margin: 1rem 0;
        }
        
        /* Make tabs more mobile-friendly */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px !important;
            padding: 8px !important;
            border-radius: 15px !important;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
            -ms-overflow-style: none;
        }
        
        .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
            display: none;
        }
        
        .stTabs [data-baseweb="tab"] {
            min-width: 80px !important;
            height: 50px !important;
            padding: 8px 12px !important;
            font-size: 14px !important;
            border-radius: 10px !important;
            flex-shrink: 0;
            text-align: center;
            white-space: nowrap;
        }
        
        .stTabs [aria-selected="true"] {
            transform: none !important;
            font-weight: 700 !important;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            transform: none !important;
        }
    }
    
    /* Desktop Navigation Tabs Styling */
    @media (min-width: 769px) {
        .mobile-nav-container {
            display: none;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            padding: 15px 20px;
            border-radius: 20px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
            margin: 1rem 0 2rem 0;
            width: 100%;
            max-width: none;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 60px;
            min-width: 140px;
            width: auto;
            flex: 1;
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            color: white;
            font-weight: 600;
            font-size: 16px;
            border: 2px solid transparent;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
            padding: 12px 20px;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(45deg, #FFD700, #FFA500);
            color: #333;
            border: 2px solid #FFD700;
            box-shadow: 0 6px 20px rgba(255,215,0,0.4);
            transform: translateY(-3px);
            font-weight: 700;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: rgba(255,255,255,0.25);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
            border: 2px solid rgba(255,255,255,0.3);
        }
    }
    
    .header-container {
        background: linear-gradient(135deg, #FFD700, #FF6B35, #7209b7);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: .5rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .event-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .significance-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .registration-container {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 0.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        margin-bottom: 1rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        color: white;
    }
    
    .form-section {
        background: rgba(255,255,255,0.95);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
    }
    
    .gallery-container {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .video-container {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Enhanced Button Styling */
    .stButton > button {
        background: linear-gradient(45deg, #FF6B35, #F7931E);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.8rem 2rem;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255,107,53,0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255,107,53,0.4);
        background: linear-gradient(45deg, #F7931E, #FF6B35);
    }
    
    /* Form Submit Button Special Styling */
    .stForm .stButton > button {
        background: linear-gradient(45deg, #28a745, #20c997);
        width: 100%;
        padding: 1rem 2rem;
        font-size: 18px;
        font-weight: bold;
        border-radius: 30px;
        box-shadow: 0 6px 20px rgba(40,167,69,0.3);
    }
    
    .stForm .stButton > button:hover {
        background: linear-gradient(45deg, #20c997, #28a745);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(40,167,69,0.4);
    }
    
    .metric-container {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Input Field Styling */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #4facfe;
        box-shadow: 0 0 10px rgba(79,172,254,0.3);
    }
    
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #4facfe;
        box-shadow: 0 0 10px rgba(79,172,254,0.3);
    }
    
    .stNumberInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #4facfe;
        box-shadow: 0 0 10px rgba(79,172,254,0.3);
    }
    
    /* Checkbox Styling */
    .stCheckbox > label {
        font-weight: 500;
        color: #333;
    }
    
    /* Progress Steps Styling */
    .progress-step {
        display: inline-block;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: linear-gradient(45deg, #4facfe, #00f2fe);
        color: white;
        text-align: center;
        line-height: 30px;
        font-weight: bold;
        margin-right: 10px;
    }
    
    .step-active {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: #333;
        box-shadow: 0 2px 8px rgba(255,215,0,0.4);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header Section
    st.markdown("""
    <div class="header-container">
        <h1>🎉 ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ 2025 🎉</h1>
        <h4>Kannada Rajyotsava Celebration</h2>
        <h4>15th November 2025 || Jabeel Park || 10 AM to 4 PM</h4>
        <h4>EK Employees & Families Special Event</h3>
        <p style="font-size: 1.2em; margin-top: .2rem;">
            Join us for a memorable celebration of Karnataka's rich heritage and culture!
        </p>
        <p> “ನಮ್ಮ ಭಾಷೆ, ನಮ್ಮ ಸಂಸ್ಕೃತಿ, ನಮ್ಮ ಒಗ್ಗಟ್ಟು” — ಇದೇ ಎಮಿರೇಟ್ಸ್ ಕನ್ನಡಿಗರ ಶಕ್ತಿ ✨</p>
        
    </div>
    """, unsafe_allow_html=True)
    
    # Simple Mobile Navigation Message
    st.markdown("""
    <div class="mobile-nav-container">
        <div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
                    padding: 15px; border-radius: 15px; color: white; text-align: center; 
                    font-weight: 600; margin: 1rem 0;">
            📱 On Mobile: Swipe left/right between tabs       </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation Tabs (Desktop)
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Home", "🎭 Event", "📸 Gallery", "🏛️ History", "📝 Register"])
    
    # Determine which tab to show based on mobile selection
    mobile_tab_mapping = {
        "🏠 Home": 0,
        "🎭 Event": 1, 
        "📸 Gallery": 2,
        "🏛️ History": 3,
        "📝 Register": 4
    }
    
    # HOME TAB
    with tab1:
        st.markdown('<div id="home-content">', unsafe_allow_html=True)
        st.markdown("### Welcome to Kannada Rajyotsava 2025!")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            #### About This Event
            We are excited to invite you and your families to the **Kannada Rajyotsava celebration** on 
            **November 15th, 2025** at **Jabeel Park** from **10 AM to 4 PM**.
            
            This special event celebrates Karnataka's rich cultural heritage and brings together EK employees 
            and their families for a day of traditional activities, performances, and community bonding.
            
            #### What Makes This Special?
            - **Exclusive Event**: Only for EK employees and their families
            - **Cultural Immersion**: Traditional Kannada performances and activities
            - **Family Fun**: Activities for all age groups
            - **Community Building**: Connect with colleagues and their families
            - **Heritage Celebration**: Honor Karnataka's formation and culture
            """)
        
        with col2:
            st.markdown("#### Quick Event Info")
            st.metric("Event Date", "Nov 15, 2025", "Special Day")
            st.metric("Day", "Saturday", "10 AM - 4 PM")
            # st.metric("Expected Attendees", "200+", "Families Welcome")
            st.metric("Venue", "Jabeel Park", "Beautiful Location")
        
        # Call to Action for Registration
        st.markdown("---")
        st.markdown("### 🎯 Ready to Join Us?")
        with st.form("registration_form-home"):
                # st.markdown('<div class="form-section">', unsafe_allow_html=True)

                # All questions in compact layout
                col1, col2 = st.columns(2)
                with col1:
                    name = st.text_input("Full Name *", placeholder="Enter your full name")
                with col2:
                    phone = st.text_input("Phone Number *", placeholder="+XXX XXXXX XXXXX")

                # Total attendees question in same line
                col1, col2, col3 = st.columns([4, 2, 2])
                with col1:
                    st.markdown("**Total Number of People Attending (including yourself and family):**")
                with col2:
                    adults = st.number_input("Adults (12+ years)", min_value=0, max_value=5, value=0)
                with col3:
                    children = st.number_input("Children (under 12)", min_value=0, max_value=5, value=0)

                colA, colB = st.columns(2)
                with colA:
                    kids_talent_show = st.radio("Will your kids participate in Kid's Talent Show?",
                                                ["Yes", "No", "Not Applicable"], horizontal=True)
                with colB:
                    email = st.text_input("Email Address", placeholder="Enter your email address")
                # Compact consent section
                consent_text = f"I voluntarily agree to attend with {(int(adults) + int(children))} total people and consent to images/videos for social media use."
                main_consent = st.checkbox(consent_text)

                st.markdown('</div>', unsafe_allow_html=True)

                # Submit Button
                submitted = st.form_submit_button("🎉 Register Now")
                st.markdown("""Contact Us : emirateskannadigaru@gmail.com for any information.""")
                if submitted:
                    if not all([name, phone]) or not main_consent:
                        st.error("❌ Please fill all fields and accept both agreements.")
                    else:
                        with st.spinner("Processing..."):
                            registration_data = {
                                'name': name,
                                'phone': phone,
                                'adults': adults,
                                'children': children,
                                'total_attendees': adults + children,
                                'kids_talent_show': kids_talent_show,
                                'main_consent': main_consent,
                                'email': email
                            }

                            if send_email_simplified(registration_data):
                                st.success(f"🎉 Registration successful! Welcome {name}!")
                                st.balloons()
                                st.info(
                                    f"**Registered:** {name} | **Phone:** {phone} | **Total:** {adults + children} people | **Kids Show:** {kids_talent_show}")
                            else:
                                st.error("❌ Registration failed. Please try again.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # EVENT TAB
    with tab2:
        st.markdown('<div id="event-content">', unsafe_allow_html=True)
        st.markdown("### 🎭 Event Details & Activities")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Event Details Box
            st.markdown('<div class="event-info">', unsafe_allow_html=True)
            st.markdown('<h3>📅 Event Details</h3>', unsafe_allow_html=True)
            st.markdown('<p><strong>Date:</strong> November 15th, 2025 (Saturday)</p>', unsafe_allow_html=True)
            st.markdown('<p><strong>Time:</strong> 10:00 AM - 4:00 PM</p>', unsafe_allow_html=True)
            st.markdown('<p><strong>Venue:</strong> Jabeel Park</p>', unsafe_allow_html=True)
            st.markdown('<p><strong>Who:</strong> EK Employees and their families only</p>', unsafe_allow_html=True)
            
            st.markdown('<h4>🎭 Event Highlights:</h4>', unsafe_allow_html=True)
            st.markdown("""
            <ul>
                <li>🎨 Traditional Kannada Dance Performances</li>
                <li>👶 Kids Talent Show (Folk Art & Cultural)</li>
                <li>🎮 Traditional Group Games & Activities</li>
                <li>🍽️ Authentic Karnataka Cuisine</li>
                <li>👗 Traditional Yellow & Red Attire Contest</li>
                <li>🎵 Karnataka Folk Music & Orchestra</li>
                <li>🏆 Rajyotsava Special Awards & Recognition</li>
                <li>📚 Kannada Literature & Poetry Corner</li>
                <li>🎶 State Anthem Group Singing</li>
            </ul>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: rgba(255,215,0,0.2); padding: 0.8rem; border-radius: 8px; margin-top: 1rem;">
                <p style="margin: 0; font-weight: bold; color: #B8860B;">
                    💡 <strong>Dress Code:</strong> Traditional attire in Karnataka flag colors (Yellow & Red) encouraged!
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### Event Schedule")
            st.markdown("""
            **🌅 10:00 AM - 11:00 AM**
            - Registration & Welcome
            - Traditional Welcome Ceremony
            
            **🎭 11:00 AM - 1:00 PM**
            - Cultural Performances
            - Kids Talent Show
            - Traditional Games
            
            **🍽️ 1:00 PM - 2:00 PM**
            - Lunch Break
            - Karnataka Cuisine Tasting
            
            **🎵 2:00 PM - 3:30 PM**
            - Folk Music & Orchestra
            - State Anthem Group Singing
            - Attire Contest Judging
            
            **🏆 3:30 PM - 4:00 PM**
            - Awards & Recognition
            - Prize Distribution
            - Closing Ceremony
            """)
        
        # Additional Event Information
        st.markdown("---")
        st.markdown("### 📋 Important Event Information")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            #### 🚗 Transportation
            - Own transportation and park at Jabeel Park
            - Metro access 
            - Carpooling encouraged
            """)
        
        with col2:
            st.markdown("""
            #### 🍽️ Food & Refreshments
            - Traditional Karnataka snacks
            - Authentic lunch 
            - Evening snacks & tea
            """)
        
        with col3:
            st.markdown("""
            #### 👥 Family Activities
            - Supervised kids play area
            - Traditional games for all ages
            - Photo booth with props
            - Cultural activity workshops
            """)
        st.markdown("### 🎯 Ready to Join Us?")
        with st.form("registration_form-event"):
            # st.markdown('<div class="form-section">', unsafe_allow_html=True)

            # All questions in compact layout
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Full Name *", placeholder="Enter your full name")
            with col2:
                phone = st.text_input("Phone Number *", placeholder="+XXX XXXXX XXXXX")

            # Total attendees question in same line
            col1, col2, col3 = st.columns([4, 2, 2])
            with col1:
                st.markdown("**Total Number of People Attending (including yourself and family):**")
            with col2:
                adults = st.number_input("Adults (12+ years)", min_value=0, max_value=5, value=0)
            with col3:
                children = st.number_input("Children (under 12)", min_value=0, max_value=5, value=0)

            colA, colB = st.columns(2)
            with colA:
                kids_talent_show = st.radio("Will your kids participate in Kid's Talent Show?",
                                            ["Yes", "No", "Not Applicable"], horizontal=True)
            with colB:
                email = st.text_input("Email Address", placeholder="Enter your email address")
            # Compact consent section
            consent_text = f"I voluntarily agree to attend with {(int(adults) + int(children))} total people and consent to images/videos for social media use."
            main_consent = st.checkbox(consent_text)

            st.markdown('</div>', unsafe_allow_html=True)

            # Submit Button
            submitted = st.form_submit_button("🎉 Register Now")
            st.markdown("""Contact Us : emirateskannadigaru@gmail.com for any information.""")
            if submitted:
                if not all([name, phone]) or not main_consent:
                    st.error("❌ Please fill all fields and accept both agreements.")
                else:
                    with st.spinner("Processing..."):
                        registration_data = {
                            'name': name,
                            'phone': phone,
                            'adults': adults,
                            'children': children,
                            'total_attendees': adults + children,
                            'kids_talent_show': kids_talent_show,
                            'main_consent': main_consent,
                            'email': email
                        }

                        if send_email_simplified(registration_data):
                            st.success(f"🎉 Registration successful! Welcome {name}!")
                            st.balloons()
                            st.info(
                                f"**Registered:** {name} | **Phone:** {phone} | **Total:** {adults + children} people | **Kids Show:** {kids_talent_show}")
                        else:
                            st.error("❌ Registration failed. Please try again.")
    # GALLERY TAB
    with tab3:
        # st.markdown("### 📸 Event Gallery")
        # st.markdown("*Memories from previous Kannada Rajyotsava celebrations and Karnataka cultural heritage*")
        
        # Image Gallery Section
        st.markdown("""
        <div class="gallery-container">
            <h3>📸 Cultural Heritage Gallery</h3>
            <p>Experience the beauty of Karnataka's traditions through these images</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Real images from Karnataka tourism and cultural events
        g1, g2, g3 = st.columns(3)
        with g1:
            st.image('static/k1.png', width="stretch")
        with g2:
            st.image('static/k4.png', width="stretch")
        with g3:
            st.image('static/k3.png', width="stretch")
        g4, g5, g6 = st.columns(3)
        with g4:
            st.image('static/k2.png', width="stretch")
        with g5:
            st.image('static/k5.png', width="stretch")
        with g6:
            st.image('static/k6.png', width="stretch")
        # YouTube Videos Section
        st.markdown("---")
        st.markdown("""
        <div class="video-container">
            <h3>🎥 Cultural Videos</h3>
            <p>Learn more about Kannada culture and previous celebrations</p>
        </div>
        """, unsafe_allow_html=True)
        
        video_cols = st.columns(2)
        
        with video_cols[0]:
            st.subheader("🎭 Karnataka Cultural Heritage")
            st.write("Karnataka Rajyotsava")
            st.video("https://www.youtube.com/watch?v=CC3TVtrgGno")  # Yakshagana performance
            
        with video_cols[1]:
            st.subheader("🏛️ Kannada Rajyotsava Celebration")
            st.write("Karnataka Rajyotsava")
            st.video("https://www.youtube.com/watch?v=m2pLKwlops4&list=RDQMHStdR16om0o&start_radio=1")  # Karnataka Rajyotsava
        
        # Additional cultural videos section
        st.markdown("### 🎵 More Cultural Videos")
        
        additional_videos = st.columns(3)
        
        with additional_videos[0]:
            st.write("**State Anthem**")
            st.video("https://www.youtube.com/watch?v=7iLvW-UYmsg")  # Jaya Bharata Jananiya Tanujate
        
        with additional_videos[1]:
            st.write("**Traditional Folk Music**")
            st.video("https://www.youtube.com/watch?v=iV4CUBQIH0M")  # Karnataka folk music
            
        with additional_videos[2]:
            st.write("**Karnataka Tourism**")
            st.video("https://www.youtube.com/watch?v=UB2Tbi_h_lw")  # Karnataka tourism highlights
        st.markdown("### 🎯 Ready to Join Us?")
        with st.form("registration_form-gallery"):
            # st.markdown('<div class="form-section">', unsafe_allow_html=True)

            # All questions in compact layout
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Full Name *", placeholder="Enter your full name")
            with col2:
                phone = st.text_input("Phone Number *", placeholder="+XXX XXXXX XXXXX")

            # Total attendees question in same line
            col1, col2, col3 = st.columns([4, 2, 2])
            with col1:
                st.markdown("**Total Number of People Attending (including yourself and family):**")
            with col2:
                adults = st.number_input("Adults (12+ years)", min_value=0, max_value=5, value=0)
            with col3:
                children = st.number_input("Children (under 12)", min_value=0, max_value=5, value=0)

            colA, colB = st.columns(2)
            with colA:
                kids_talent_show = st.radio("Will your kids participate in Kid's Talent Show?",
                                            ["Yes", "No", "Not Applicable"], horizontal=True)
            with colB:
                email = st.text_input("Email Address", placeholder="Enter your email address")
            # Compact consent section
            consent_text = f"I voluntarily agree to attend with {(int(adults) + int(children))} total people and consent to images/videos for social media use."
            main_consent = st.checkbox(consent_text)

            st.markdown('</div>', unsafe_allow_html=True)

            # Submit Button
            submitted = st.form_submit_button("🎉 Register Now")
            st.markdown("""Contact Us : emirateskannadigaru@gmail.com for any information.""")
            if submitted:
                if not all([name, phone]) or not main_consent:
                    st.error("❌ Please fill all fields and accept both agreements.")
                else:
                    with st.spinner("Processing..."):
                        registration_data = {
                            'name': name,
                            'phone': phone,
                            'adults': adults,
                            'children': children,
                            'total_attendees': adults + children,
                            'kids_talent_show': kids_talent_show,
                            'main_consent': main_consent,
                            'email': email
                        }

                        if send_email_simplified(registration_data):
                            st.success(f"🎉 Registration successful! Welcome {name}!")
                            st.balloons()
                            st.info(
                                f"**Registered:** {name} | **Phone:** {phone} | **Total:** {adults + children} people | **Kids Show:** {kids_talent_show}")
                        else:
                            st.error("❌ Registration failed. Please try again.")
    # HISTORY TAB
    with tab4:
        st.markdown("### 🏛️ Kannada Rajyotsava History & Significance")
        
        # Kannada Rajyotsava Significance Section
        st.markdown('<div class="significance-box">', unsafe_allow_html=True)
        st.markdown('<h3>🏛️ Karnataka Formation Day</h3>', unsafe_allow_html=True)
        
        st.markdown("""<p><strong>Karnataka Rajyotsava</strong> or <strong>Kannada Rajyotsava</strong>, also known as Karnataka Formation Day, 
        is celebrated on <strong>1st November</strong> every year. This historic day in <strong>1956</strong> marked when all 
        Kannada language-speaking regions of South India were merged to form the unified state of Karnataka.</p>""", unsafe_allow_html=True)
        
        st.markdown("""<p>🎊 The Rajyotsava day is a government holiday in Karnataka and is celebrated by Kannadigas worldwide. 
        Traditional celebrations include wearing <strong>Yellow and Red</strong> (Karnataka flag colors) clothing.</p>""", unsafe_allow_html=True)
        
        st.markdown('<p><strong>🎭 Traditional Celebration Features:</strong></p>', unsafe_allow_html=True)
        
        st.markdown("""
        <ul>
            <li>🏆 Rajyotsava Awards presentation by the Government of Karnataka</li>
            <li>🚩 Official Karnataka flag hoisting ceremonies (Yellow & Red colors)</li>
            <li>📜 Addresses from the Chief Minister and Governor</li>
            <li>🎵 Community festivals, orchestra performances</li>
            <li>📚 Kannada book releases and literary events</li>
            <li>🎭 Traditional folk art and cultural concerts</li>
            <li>👗 Wearing festive yellow and red traditional attire</li>
            <li>🎶 Singing the state anthem: <em>"Jaya Bharatha Jananiya Tanujate"</em></li>
        </ul>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: linear-gradient(45deg, #FFD700, #FF0000); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
            <p style="text-align: center; color: white; font-weight: bold; margin: 0;">
                🎵 State Anthem: "ಜಯ ಭಾರತ ಜನನಿಯ ತನುಜಾತೆ" (Jaya Bharatha Jananiya Tanujate)
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""<p><em>"ಕನ್ನಡ ನಾಡು ನಾಮ ಗರ್ವ, ಕನ್ನಡ ಬಾಲೆ ನಾಮ ಪ್ರೀತಿ!"</em><br>
        <small>(Karnataka is our pride, Kannada is our love!)</small></p>""", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Additional Historical Information
        st.markdown("---")
        st.markdown("### 📚 Historical Timeline")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Key Historical Events
            
            **1950s - The Unification Movement**
            - Various Kannada-speaking regions scattered across different states
            - Growing demand for linguistic reorganization
            - Formation of States Reorganisation Committee
            
            **November 1, 1956 - The Historic Day**
            - Official formation of Mysore State (later Karnataka)
            - Integration of Kannada-speaking areas
            - Birth of unified Kannada identity
            
            **1973 - Name Change**
            - Mysore State renamed to Karnataka
            - Strengthened regional identity
            """)
        
        with col2:
            st.markdown("""
            #### Cultural Significance
            
            **Language & Literature**
            - One of the oldest Dravidian languages
            - Rich literary tradition spanning centuries
            - Home to legendary poets and writers
            
            **Art & Architecture**
            - Magnificent temples and palaces
            - Traditional dance forms like Yakshagana
            - Unique folk music traditions
            
            **Modern Achievements**
            - IT capital of India (Bangalore)
            - Significant contributions to science and technology
            - Vibrant cultural festivals and celebrations
            """)
        st.markdown("### 🎯 Ready to Join Us?")
        with st.form("registration_form-history"):
            # st.markdown('<div class="form-section">', unsafe_allow_html=True)

            # All questions in compact layout
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Full Name *", placeholder="Enter your full name")
            with col2:
                phone = st.text_input("Phone Number *", placeholder="+XXX XXXXX XXXXX")

            # Total attendees question in same line
            col1, col2, col3 = st.columns([4, 2, 2])
            with col1:
                st.markdown("**Total Number of People Attending (including yourself and family):**")
            with col2:
                adults = st.number_input("Adults (12+ years)", min_value=0, max_value=5, value=0)
            with col3:
                children = st.number_input("Children (under 12)", min_value=0, max_value=5, value=0)

            colA, colB = st.columns(2)
            with colA:
                kids_talent_show = st.radio("Will your kids participate in Kid's Talent Show?",
                                            ["Yes", "No", "Not Applicable"], horizontal=True)
            with colB:
                email = st.text_input("Email Address", placeholder="Enter your email address")
            # Compact consent section
            consent_text = f"I voluntarily agree to attend with {(int(adults) + int(children))} total people and consent to images/videos for social media use."
            main_consent = st.checkbox(consent_text)

            st.markdown('</div>', unsafe_allow_html=True)

            # Submit Button
            submitted = st.form_submit_button("🎉 Register Now")
            st.markdown("""Contact Us : emirateskannadigaru@gmail.com for any information.""")
            if submitted:
                if not all([name, phone]) or not main_consent:
                    st.error("❌ Please fill all fields and accept both agreements.")
                else:
                    with st.spinner("Processing..."):
                        registration_data = {
                            'name': name,
                            'phone': phone,
                            'adults': adults,
                            'children': children,
                            'total_attendees': adults + children,
                            'kids_talent_show': kids_talent_show,
                            'main_consent': main_consent,
                            'email': email
                        }

                        if send_email_simplified(registration_data):
                            st.success(f"🎉 Registration successful! Welcome {name}!")
                            st.balloons()
                            st.info(
                                f"**Registered:** {name} | **Phone:** {phone} | **Total:** {adults + children} people | **Kids Show:** {kids_talent_show}")
                        else:
                            st.error("❌ Registration failed. Please try again.")
    # REGISTER TAB
    with tab5:
        # Simple Registration Form
        st.markdown("""
        <div class="registration-container">
            <h3 style="text-align: center; margin-bottom: 0.5rem;">📝 Event Registration</h3>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("registration_form"):
            # st.markdown('<div class="form-section">', unsafe_allow_html=True)
            
            # All questions in compact layout
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Full Name *", placeholder="Enter your full name")
            with col2:
                phone = st.text_input("Phone Number *", placeholder="+XXX XXXXX XXXXX")
            
            # Total attendees question in same line
            col1, col2, col3 = st.columns([4, 2, 2])
            with col1:
                st.markdown("**Total Number of People Attending (including yourself and family):**")
            with col2:
                adults = st.number_input("Adults (12+ years)", min_value=0, max_value=5, value=0)
            with col3:
                children = st.number_input("Children (under 12)", min_value=0, max_value=5, value=0)

            colA, colB = st.columns(2)
            with colA:
                kids_talent_show = st.radio("Will your kids participate in Kid's Talent Show?",
                                              ["Yes", "No", "Not Applicable"], horizontal=True)
            with colB:
                email = st.text_input("Email Address", placeholder="Enter your email address")
            # Compact consent section
            consent_text = f"I voluntarily agree to attend with {(int(adults)+int(children))} total people and consent to images/videos for social media use."
            main_consent = st.checkbox(consent_text)
            
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Submit Button
            submitted = st.form_submit_button("🎉 Register Now")
            st.markdown("""Contact Us : emirateskannadigaru@gmail.com for any information.""")
            if submitted:
                if not all([name, phone]) or not main_consent:
                    st.error("❌ Please fill all fields and accept both agreements.")
                else:
                    with st.spinner("Processing..."):
                        registration_data = {
                            'name': name,
                            'phone': phone,
                            'adults': adults,
                            'children': children,
                            'total_attendees': adults+children,
                            'kids_talent_show': kids_talent_show,
                            'main_consent': main_consent,
                            'email': email
                        }
                        
                        if send_email_simplified(registration_data):
                            st.success(f"🎉 Registration successful! Welcome {name}!")
                            st.balloons()
                            st.info(f"**Registered:** {name} | **Phone:** {phone} | **Total:** {adults+children} people | **Kids Show:** {kids_talent_show}")
                        else:
                            st.error("❌ Registration failed. Please try again.")
        st.markdown("----")
        st.image('static/k7.png', width="stretch")
def send_email_simplified(registration_data):
    """Simplified email function for new registration form"""
    try:
        # Email configuration - you'll need to set these in Streamlit secrets
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Try different ways to access secrets
        try:
            sender_email = st.secrets["gmail"]["GMAIL_USER"]
            sender_password = st.secrets["gmail"]["GMAIL_PASSWORD"]
        except:
            try:
                sender_email = st.secrets["GMAIL_USER"]
                sender_password = st.secrets["GMAIL_PASSWORD"]
            except Exception as e:
                print(e)
                # Fallback to environment variables
                sender_email = "emirateskannadigaru@gmail.com"
                sender_password = "sicyfifhuudhbkvl"
                pass
        
        if not sender_email or not sender_password:
            # Save to local file as backup
            with open("registrations.txt", "a", encoding="utf-8") as f:
                f.write(f"\n--- Registration at {datetime.now()} ---\n")
                f.write(f"Name: {registration_data['name']}\n")
                f.write(f"Phone: {registration_data['phone']}\n")
                f.write(f"Adults (12+ years): {registration_data['adults']}\n")
                f.write(f"Children (under 12): {registration_data['children']}\n")
                f.write(f"Total Attendees: {registration_data['total_attendees']}\n")
                f.write(f"Kids Talent Show: {registration_data['kids_talent_show']}\n")
                f.write(f"Consents: Main={registration_data['main_consent']}\n")
                f.write("-" * 50 + "\n")
            return True
        email = registration_data['email']
        to_email = sender_email
        if email:
            to_email = email
        cc_emails = [sender_email, 'prashanthme38@gmail.com']
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email  # Send to yourself
        msg["Cc"] = ",".join(cc_emails)
        msg['Subject'] = f"Kannada Rajyotsava 2025 Registration - {registration_data['name']}"
        
        # Simplified email body
        body = f"""
        🎉 NEW REGISTRATION - Kannada Rajyotsava 2025 🎉
        
        EVENT DETAILS:
        📅 Date: November 15th, 2025
        ⏰ Time: 10 AM - 4 PM
        📍 Venue: Jabeel Park
        
        REGISTRATION INFORMATION:
        👤 Name: {registration_data['name']}
        📱 Phone: {registration_data['phone']}
        
        FAMILY DETAILS:
        👥 Adults (12+ years): {registration_data['adults']}
        👶 Children (under 12): {registration_data['children']}
        📊 Total Attendees: {registration_data['total_attendees']}
        
        PARTICIPATION:
        🎭 Kids Talent Show: {registration_data['kids_talent_show']}
        
        CONSENTS:
        ✅ Event & Social Media Consent: {'Yes' if registration_data['main_consent'] else 'No'}
        
        Registration Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        try:
            server.sendmail(sender_email, to_email, text)
        except Exception as e:
            server.sendmail(sender_email, sender_email, text)
        server.quit()
        return True
    except Exception as e:
        print("Error:", str(e))
        st.error(f"Failed to send email: {str(e)}")
        return False

def send_email_enhanced(registration_data):
    """Enhanced email function for detailed registration data"""
    try:
        # Try different ways to access secrets
        try:
            sender_email = st.secrets["gmail"]["GMAIL_USER"]
            sender_password = st.secrets["gmail"]["GMAIL_PASSWORD"]
        except:
            try:
                sender_email = st.secrets["GMAIL_USER"]
                sender_password = st.secrets["GMAIL_PASSWORD"]
            except:
                # Fallback to environment variables
                sender_email = os.getenv("GMAIL_USER", "")
                sender_password = os.getenv("GMAIL_PASSWORD", "")
        
        if not sender_email or not sender_password:
            # Save to local file as backup
            with open("registrations.txt", "a", encoding="utf-8") as f:
                f.write(f"\n--- Registration at {datetime.now()} ---\n")
                for key, value in registration_data.items():
                    f.write(f"{key}: {value}\n")
                f.write("-" * 50 + "\n")
            return True
        
        # Create enhanced email
        cc_emails = [sender_email, 'javabit041@gmail.com']
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email  # Send to yourself
        msg["Cc"] = ", ".join(cc_emails)
        msg['Subject'] = f"Kannada Rajyotsava 2025 Registration - {registration_data['name']}"
        
        # Enhanced email body
        body = f"""
        🎉 NEW REGISTRATION - Kannada Rajyotsava 2025 🎉
        
        EVENT DETAILS:
        📅 Date: November 15th, 2025
        ⏰ Time: 10 AM - 4 PM
        📍 Venue: Jabeel Park
        
        REGISTRANT INFORMATION:
        👤 Name: {registration_data['name']}
        📧 Email: {registration_data['email']}
        📱 Phone: {registration_data['phone']}
        🆔 Employee ID: {registration_data.get('employee_id', 'Not provided')}
        
        FAMILY & PREFERENCES:
        👨‍👩‍👧‍👦 Family Members: {registration_data['family_members']}
        {f"Family Details: {registration_data['family_details']}" if registration_data['family_details'] else ""}
        🍽️ Dietary Preference: {registration_data['dietary_preference']}
        🚗 Transportation: {registration_data['transportation']}
        👕 T-Shirt Size: {registration_data['tshirt_size']}
        
        PARTICIPATION:
        🎭 Cultural Activities: {', '.join(registration_data['cultural_participation']) if registration_data['cultural_participation'] else 'None selected'}
        🤝 Volunteer: {'Yes' if registration_data['volunteer'] else 'No'}
        📸 Photography Help: {'Yes' if registration_data['photography'] else 'No'}
        
        SPECIAL REQUIREMENTS:
        {registration_data['special_requirements'] if registration_data['special_requirements'] else 'None'}
        
        EMERGENCY CONTACT:
        {registration_data['emergency_contact'] if registration_data['emergency_contact'] else 'Not provided'}
        
        CONSENTS:
        📷 Photo Consent: {'Yes' if registration_data['photo_consent'] else 'No'}
        🏥 Health Consent: {'Yes' if registration_data['health_consent'] else 'No'}
        📜 Terms Consent: {'Yes' if registration_data['terms_consent'] else 'No'}
        
        Registration Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Total Attendees for this registration: {registration_data['family_members'] + 1}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, sender_email, text)
        server.quit()
        
        return True
    except Exception as e:
        st.error(f"Failed to send email: {str(e)}")
        return False
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; border-radius: 10px; margin-top: 2rem;">
        <h4>🎊 Join Us in Celebrating Karnataka's Rich Heritage! 🎊</h4>
        <p>For any queries, contact: <a href="mailto:events@company.com" style="color: #FFD700;">events@company.com</a></p>
        <p><em>ಜೈ ಕರ್ನಾಟಕ ಮಾತೆ! • Long Live Mother Karnataka!</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()