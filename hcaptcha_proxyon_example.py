from anticaptchaofficial.hcaptchaproxyon import *

# Non-Enterprise version
solver = hCaptchaProxyon()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")
solver.set_proxy_address("PROXY_ADDRESS")
solver.set_proxy_port(1234)
solver.set_proxy_login("proxylogin")
solver.set_proxy_password("proxypassword")
solver.set_user_agent("Mozilla/5.0")
solver.set_cookies("test=true")

# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print("g-response: "+g_response)
    print("user-agent, use it to post the form: ", solver.get_user_agent())
    print("respkey, if any: ", solver.get_respkey())
else:
    print("task finished with error "+solver.error_code)


# Enterprise version
solver = hCaptchaProxyon()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("https://website.com")
solver.set_website_key("SITE_KEY")
solver.set_proxy_address("PROXY_ADDRESS")
solver.set_proxy_port(1234)
solver.set_proxy_login("proxylogin")
solver.set_proxy_password("proxypassword")
solver.set_user_agent("Mozilla/5.0")
solver.set_cookies("test=true")
solver.set_enterprise_payload({
    "rqdata": "rq data value from target website",
    "sentry": True,
    # ... etc, see https://anti-captcha.com/apidoc/task-types/HCaptchaTask for more
})

g_response = solver.solve_and_return_solution()
if g_response != 0:
    print("g-response: "+g_response)
else:
    print("task finished with error "+solver.error_code)
