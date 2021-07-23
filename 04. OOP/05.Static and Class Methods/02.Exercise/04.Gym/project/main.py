from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

customer1 = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment1 = Equipment("Treadmill")
trainer1 = Trainer("Peter")
subscription1 = Subscription("14.05.2020", 1, 1, 1)
plan1 = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer1)
gym.add_equipment(equipment1)
gym.add_trainer(trainer1)
gym.add_plan(plan1)
gym.add_subscription(subscription1)

print(Customer.get_next_id())
# print(Customer.get_next_id())
# print(Customer.get_next_id())

print(gym.subscription_info(1))
