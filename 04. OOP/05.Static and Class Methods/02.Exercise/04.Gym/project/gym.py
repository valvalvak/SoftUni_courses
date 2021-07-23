from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        """add the customer in the customer list, if the customer is not already in it"""
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        """add the trainer to the trainers list, if the trainer is not already in it"""
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        """add the equipment to the equipment list, if the equipment is not already in it"""
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        """add the plan to the plans list, if the plan is not already in it"""
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        """add the subscription in the subscriptions list, if the subscription is not already in it"""
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        """get the subscription, the customer and trainer, the plan and the equipment.
        Then return their string representations each on a new line."""
        result = ""
        result += '\n'.join([repr(obj) for obj in self.subscriptions]) + '\n'
        result += '\n'.join([repr(obj) for obj in self.customers]) + '\n'
        result += "\n".join([repr(obj) for obj in self.trainers]) + '\n'
        result += "\n".join([repr(obj) for obj in self.plans]) + '\n'
        result += "\n".join([repr(obj) for obj in self.equipment])
        return result
