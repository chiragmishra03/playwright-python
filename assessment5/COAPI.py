from playwright.sync_api import Playwright


class ApiUtils:
    BASE_URL = "https://rahulshettyacademy.com"

    def _get_api_context(self, playwright: Playwright):
        return playwright.request.new_context(base_url=self.BASE_URL)

    def getToken(self, playwright: Playwright):
        payload = {
            "userEmail": "Shubhamlambha.1996@gmail.com",
            "userPassword": "Shubh123"
        }

        context = self._get_api_context(playwright)
        response = context.post(
            "/api/ecom/auth/login",
            data=payload,
            headers={"content-type": "application/json"}
        )

        response_json = response.json()
        return response_json["token"]

    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)

        payload = {
            "orders": [
                {
                    "country": "India",
                    "productOrderedId": "68a961459320a140fe1ca57a"
                }
            ]
        }

        context = self._get_api_context(playwright)
        response = context.post(
            "/api/ecom/order/create-order",
            data=payload,
            headers={
                "authorization": token,
                "content-type": "application/json"
            }
        )

        response_json = response.json()
        return response_json["orders"][0]
