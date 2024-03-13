1. ls -al ~/.ssh
    ssh-keygen -t ed25519 -C "email"
    eval "$(ssh-agent -s)"
2. скопировать ssh ключ из файла и вставить в аккаунт на github
3. git clone git@github.com:username/rep