# 🎉 Kannada Rajyotsava 2025 - EK Celebration App

A beautiful Streamlit web application for the Kannada Rajyotsava celebration event, featuring registration form with email notifications, image gallery, and YouTube videos.

## 🌟 Features

- **Event Information**: Complete details about the Kannada Rajyotsava celebration
- **Registration Form**: Interactive form with email notification system
- **Image Gallery**: Showcase of previous event memories
- **YouTube Videos**: Embedded videos about Kannada culture
- **Significance Section**: Educational content about Karnataka Rajyotsava
- **Beautiful UI**: Gradient designs and responsive layout

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Email Settings

Edit `.streamlit/secrets.toml` and add your Gmail credentials:

```toml
[gmail]
GMAIL_USER = "your-email@gmail.com"
GMAIL_PASSWORD = "your-app-password"
```

**Important**: Use Gmail App Password, not your regular password!

### 3. Run the Application

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## 📧 Email Setup Instructions

### For Gmail:

1. Enable 2-Step Verification on your Google Account
2. Go to Google Account > Security > 2-Step Verification > App passwords
3. Generate a new App Password for "Mail"
4. Use this 16-digit password in the `secrets.toml` file

### Alternative Environment Variables:

You can also set environment variables instead of using secrets.toml:

```bash
export GMAIL_USER="your-email@gmail.com"
export GMAIL_PASSWORD="your-app-password"
```

## 🎨 Customization

### Adding Real Images:

Replace placeholder images in the gallery section:

```python
sample_images = [
    "path/to/your/image1.jpg",
    "path/to/your/image2.jpg",
    # Add more image paths
]
```

### Adding Real YouTube Videos:

Replace placeholder video URLs:

```python
st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")
```

### Styling:

Modify the CSS in the `st.markdown()` sections to change colors, fonts, and layouts.

## 📁 Project Structure

```
ek-kannda/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .streamlit/
│   └── secrets.toml           # Email configuration (keep private)
└── README.md                  # This file
```

## 🎯 Event Details

- **Date**: November 15th, 2025
- **Time**: 10:00 AM - 4:00 PM  
- **Venue**: Jabeel Park
- **Audience**: EK Employees and their families

## 🔧 Troubleshooting

### Email Not Sending:
- Verify Gmail App Password is correct
- Check if 2-Step Verification is enabled
- Ensure secrets.toml file exists and has correct format

### App Not Loading:
- Verify all dependencies are installed
- Check Python version compatibility
- Run `streamlit doctor` for diagnostics

## 📝 Registration Form Fields

- Full Name (Required)
- Email Address (Required)
- Phone Number (Required)
- Number of Family Members
- Special Requirements
- Emergency Contact
- Consent Checkboxes

## 🎊 About Kannada Rajyotsava

Karnataka Rajyotsava, celebrated on November 1st, commemorates the formation of Karnataka state in 1956 when all Kannada-speaking regions were unified. This special EK celebration brings together employees and families to honor Karnataka's rich cultural heritage.

## 🤝 Support

For technical issues or questions about the event, contact: events@company.com

---

**ಜೈ ಕರ್ನಾಟಕ ಮಾತೆ! • Long Live Mother Karnataka!** 🏛️