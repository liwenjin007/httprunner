from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseMubuLogin(HttpRunner):
    config = Config("testcase description")

    teststeps = [
        Step(
            RunRequest("/v3/api/user/phone_login")
                .post("https://api2.mubu.com/v3/api/user/phone_login")
                .with_headers(
                **{
                    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                    "version": "3.0.0-2.0.0.1934",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                    "data-unique-id": "deead2a0-bd7b-4432-9632-3d1dd82cb940",
                    "content-type": "application/json;charset=UTF-8",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMjU0NzY0ODAiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2OTM4MDQwNDksImlhdCI6MTY5MTIxMjA0OX0.JcwAqIV9l1-9gazjGa0Tz0v6JITcR0gfd8Yw6ABu3MF1-G92Hb5wOxq41upa8AVgWxCTy7o_nI_6Zo29kc6Nvw",
                    "x-request-id": "63ec7e4a-00a4-4543-b74b-3ebba5c87fe7",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                }
            )
                .with_json(
                {"phone": "18245297665", "password": "123456lwj", "callbackType": 0}
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/app")
                .get("https://mubu.com/app")
                .with_headers(
                **{
                    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/user/profile")
                .post("https://api2.mubu.com/v3/api/user/profile")
                .with_headers(
                **{
                    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                    "data-unique-id": "deead2a0-bd7b-4432-9632-3d1dd82cb940",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMjU0NzY0ODAiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2OTM4MDU4MTksImlhdCI6MTY5MTIxMzgxOX0.H6jQIQpNU3m0xSvNJ79XwEGuobUR1L125c9bGg8LPgKo2NebAAWE2RrB5iCwE2-iO5fMf0LLlWHteh0g39x5Uw",
                    "x-request-id": "8ade82b2-2cc7-4074-b5c2-fbc4c2d667cf",
                    "version": "3.0.0-2.0.0.1934",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                }
            )
                .with_data("")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_user_params")
                .post("https://api2.mubu.com/v3/api/user/get_user_params")
                .with_headers(
                **{
                    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                    "data-unique-id": "deead2a0-bd7b-4432-9632-3d1dd82cb940",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMjU0NzY0ODAiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2OTM4MDU4MTksImlhdCI6MTY5MTIxMzgxOX0.H6jQIQpNU3m0xSvNJ79XwEGuobUR1L125c9bGg8LPgKo2NebAAWE2RrB5iCwE2-iO5fMf0LLlWHteh0g39x5Uw",
                    "x-request-id": "edff795a-e61c-4983-a77d-c2048d5ce6f0",
                    "version": "3.0.0-2.0.0.1934",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                }
            )
                .with_data("")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_onboard_state")
                .post("https://api2.mubu.com/v3/api/user/get_onboard_state")
                .with_headers(
                **{
                    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                    "version": "3.0.0-2.0.0.1934",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                    "data-unique-id": "deead2a0-bd7b-4432-9632-3d1dd82cb940",
                    "content-type": "application/json;charset=UTF-8",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMjU0NzY0ODAiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2OTM4MDU4MTksImlhdCI6MTY5MTIxMzgxOX0.H6jQIQpNU3m0xSvNJ79XwEGuobUR1L125c9bGg8LPgKo2NebAAWE2RrB5iCwE2-iO5fMf0LLlWHteh0g39x5Uw",
                    "x-request-id": "f1fb1511-f3fb-4d41-947a-5b064b63c392",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                }
            )
                .with_json({})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseMubuLogin().test_start()