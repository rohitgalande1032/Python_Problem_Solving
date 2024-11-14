class OTTSubscription:
    def __init__(self, sub_id, plan, price):
        self.sub_id = sub_id
        self.plan = plan
        self.price = price

    def subscribe(self):
        print(f"Subscriber with {self.sub_id} id subscribed to {self.plan} plan")

    def unsubscribe(self):
        print(f"Subscriber with {self.sub_id} unsubscribed to {self.plan} plan")


class PremiumSubscription(OTTSubscription):
    def __init__(self, sub_id, plan, price, screen_size):
        super().__init__(sub_id, plan, price)
        self.screen_size = screen_size

    def set_max_size(self):
        print(f"Maximum size set to {self.screen_size} in premium plan")


user1 = OTTSubscription(12234, "Monthly", 199)
user1.subscribe()
user1.unsubscribe()

premium_user = PremiumSubscription(122235, "Yearly", 499, 4)
premium_user.subscribe()
premium_user.unsubscribe()
premium_user.set_max_size()