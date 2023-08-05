from httprunner import HttpRunner, Config, Step, RunRequest


class CaseMubuLogin(HttpRunner):
    config = (Config("testcase description")
              .base_url("https://api2.$host")
              .verify(False)
              .variables(**{
            "data_unique_id": "deead2a0-bd7b-4432-9632-3d1dd82cb940",
            "memberId": "4441534322996672",
            "host": "${get_test_env()}"
        })
              .export("jwt_token", "user_id")
    )

    teststeps = [
        Step(
            RunRequest("/v3/api/user/phone_login")
                .with_variables(**{
                "phone": "18245297665",
                "password": "123456lwj",
                "callbackType": 0
            })
                .post("/v3/api/user/phone_login")
                .with_headers(
                **{
                    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                    "version": "3.0.0-2.0.0.1934",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                    "data-unique-id": "$data_unique_id",
                    "content-type": "application/json;charset=UTF-8",
                    "jwt-token": "",
                    "x-request-id": "${gen_random_request_id()}",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                }
            )
                .with_json(
                {"phone": "$phone", "password": "$password", "callbackType": "$callbackType"}
            )
                .teardown_hook("${get_response($response)}", "phone")
                .extract()
                # .with_jmespath("body.data.token", "jwt-token")
                .with_jmespath('cookies."Jwt-Token"', "jwt_token")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("$phone", 18245297665)
        ),
        Step(
            RunRequest("/v3/api/user/profile")
                .post("/v3/api/user/profile")
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
                .extract()
                .with_jmespath("body.data.id", "user_id")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
        ),

    ]


if __name__ == "__main__":
    CaseMubuLogin().test_start()
