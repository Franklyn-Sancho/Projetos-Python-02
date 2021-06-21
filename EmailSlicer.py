#!/usr/bin/python3

email = input('Qual o seu endereço de email?: ').strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
res = f"Seu usernema is '{user_name}' and your domain name is '{domain_name}"
print(res)