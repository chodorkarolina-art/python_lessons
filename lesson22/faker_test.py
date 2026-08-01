# lesson22_task5

from faker import Faker

# tworzymy generator polskich danych
fake = Faker("pl_PL")

print("=== 10 losowych osób ===")

for i in range(10):
    print(f"{i + 1}. {fake.name()}")

print()

print("=== 10 losowych zdań ===")

for i in range(10):
    print(f"{i + 1}. {fake.sentence()}")