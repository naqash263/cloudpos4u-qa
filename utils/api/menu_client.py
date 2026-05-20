class MenuClient:
    def get_all_dishes(self):
        return self.request(
            method="get",
            endpoint="/dish/all"
        )

    def get_all_dishes_with_custom_headers(self, headers=None, cookies=None):
        return self.request(
            method="get",
            endpoint="/dish/all",
            headers=headers or {},
            cookies=cookies or {},
            auth=False
        )