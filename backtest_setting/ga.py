import random

# 该需求实际上是一个典型的参数优化问题，选择遗传算法主要是为了平衡效率与效果，快速找到最优参数组合（a、b、c）。
# 每个关键步骤和参数配置都有其生物学意义，比如“选择”对应自然选择，“变异”和“交叉”对应基因变异和重组，这种模拟自然进化的过程非常适合非线性和复杂的搜索问题。

# 参数范围
RANGE_A = (1, 100)
RANGE_B = (6, 100)
RANGE_C = (10, 50)
# 参数配置
POPULATION_SIZE = 10
MUTATION_PROB = 0.6
RETAIN_RATIO = 0.6
MAX_ITERATIONS = 5


# 初始化种群
def initialize_population():
    return [
        {"a": random.randint(*RANGE_A),
         "b": random.randint(*RANGE_B),
         "c": random.randint(*RANGE_C)}
        for _ in range(POPULATION_SIZE)
    ]


# 损益评估函数 (需要用户自定义实现)
def evaluate_fitness(individual):
    # 示例：损益 = 100 - (a + b + c) (需替换为实际评估逻辑)
    return 100 - (individual["a"] + individual["b"] + individual["c"])


# 变异操作
def mutate(individual):
    param = random.choice(["a", "b", "c"])
    if param == "a":
        individual["a"] = random.randint(*RANGE_A)
    elif param == "b":
        individual["b"] = random.randint(*RANGE_B)
    else:
        individual["c"] = random.randint(*RANGE_C)
    return individual


# 交叉操作
def crossover(parent1, parent2):
    point = random.choice(["a", "b", "c"])
    child = parent1.copy()
    child[point] = parent2[point]
    return child


# 主遗传算法
def genetic_algorithm():
    population = initialize_population()

    for iteration in range(MAX_ITERATIONS):
        # 评估适应度
        population = sorted(population, key=evaluate_fitness, reverse=True)
        print(f"Iteration {iteration + 1}: Best fitness = {evaluate_fitness(population[0])}")

        # 选择精英
        retain_length = int(POPULATION_SIZE * RETAIN_RATIO)
        retained = population[:retain_length]

        # 生成后代
        new_generation = retained[:]
        while len(new_generation) < POPULATION_SIZE:
            if random.random() < MUTATION_PROB:
                # 变异
                new_generation.append(mutate(random.choice(retained).copy()))
            else:
                # 交叉
                parent1, parent2 = random.sample(retained, 2)
                new_generation.append(crossover(parent1, parent2))

        population = new_generation

    # 输出最佳参数
    best_individual = max(population, key=evaluate_fitness)
    return best_individual


# 执行遗传算法
best_parameters = genetic_algorithm()
print("最佳参数：", best_parameters)
