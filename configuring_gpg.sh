#small bash script to configure gpg
#!/bin/bash

echo "Generating a new GPG key..."

# Setting the email address associated with the GPG key
read -p "Enter your email address: " email

# Set the key type and key length
key_type="RSA"
key_length="4096"

# Set the expiration period for the key
expiration="0" # 0 means the key does not expiree

# Generate the GPG key
gpg --batch --full-generate-key <<EOF
    Key-Type: $key_type
    Key-Length: $key_length
    Name-Real: User
    Name-Email: $email
    Expire-Date: $expiration
    %commit
EOF

echo "GPG key generated successfully."
