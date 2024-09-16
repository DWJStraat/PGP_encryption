from crypto.crypt import encrypt_message
from mailvelope.keys import download_public_key_from_mailvelope

if __name__ == '__main__':
    print("Who do you want to send the email to? (Enter your email address)")
    recipient_email = input()
    print("What is the content of the email?")
    email_content = input()

    public_key = download_public_key_from_mailvelope(recipient_email)

    encrypted_email = encrypt_message(email_content, public_key)

    print("Encrypted email:", encrypted_email)
