import random

def simulate_dice_roll(num_simulations):
    results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(num_simulations):
        roll_result = random.randint(1, 6)
        results[roll_result] += 1

    return results

def calculate_probabilities(results, num_simulations):
    probabilities = {key: value / num_simulations for key, value in results.items()}
    return probabilities

def main():
    num_simulations = int(input("주사위를 몇 번 던질까요? "))

    results = simulate_dice_roll(num_simulations)
    probabilities = calculate_probabilities(results, num_simulations)

    print("\n결과:")
    for number, count in results.items():
        print(f"{number}이(가) 나온 횟수: {count}")

    print("\n확률:")
    for number, probability in probabilities.items():
        print(f"{number}이(가) 나올 확률: {probability:.2%}")

if __name__ == "__main__":
    main()
