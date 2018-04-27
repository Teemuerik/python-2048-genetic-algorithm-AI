# -*- coding: utf-8 -*-
from game import game as G
import math
import os
import sys
from random import randint
import random
from collections import deque
import numpy as np
import time

class Neural_Network(object):
    def __init__(self, weights_list = None, chromosome = None):
        self.fitness = 1 #how fit it is to reproduce (based on the final score in the game)
 
        self.input_layer_size = 16
        self.output_layer_size = 4
        self.hidden_layer_sizes = [8]

        self.W = []
        if weights_list:
            if len(weights_list) != len(self.hidden_layer_sizes) + 1:
                assert False, "Weights list's lenght should be %s, not %s" % (len(self.hidden_layer_sizes) + 1, len(weights_list))
            for weight in weights_list:
                self.W.append(weight)
        else:
            self.W.append(np.random.randn(self.input_layer_size,self.hidden_layer_sizes[0]))
            for weight_index in range(1, len(self.hidden_layer_sizes)):
                self.W.append(np.random.randn(self.hidden_layer_sizes[weight_index-1], self.hidden_layer_sizes[weight_index]))
            self.W.append(np.random.randn(self.hidden_layer_sizes[-1],self.output_layer_size))

        self.weights = []
        self.weights.extend(self.W)
 
        if chromosome:
            self.decode_chromosome(chromosome)
 
 
 
 
 
        self.get_chromosome()
 
    def forward(self,X):
        #propagate inputs through network
        self.z = []
        self.a = []
        self.z.append(np.dot(X, self.W[0]))
        for index in range(1, len(self.hidden_layer_sizes)+1):
            self.a.append(self.activation(self.z[index-1]))
            self.z.append(np.dot(X,self.W[index]))
        result = self.activation(self.z[-1])
        return result > .5
 
    def activation(self,z):
        return 1/(1+np.exp(-z))
 
    def get_weight(self,n):
        return self.weights[n]
 
    def get_fitness(self):
        return self.fitness
 
    def get_chromosome(self):
        self.chromosome = []
        for weight_list in self.weights:
            for row in weight_list:
                for weight in row:
                    self.chromosome.append(weight)
    def decode_chromosome(self,c):
        chromo = c[::-1]
        new_weights = []
        for weight_list in self.weights:
            new_weight_list = []
            for row in weight_list:
                new_row = []
                for _ in row:
                    weight = chromo.pop()
                    new_row.append(weight)
                new_weight_list.append(new_row)
            new_weights.append(new_weight_list)
        self.weights = new_weights
        for weight_index in range(len(self.weights)-1):
            self.W[weight_index] = self.weights[weight_index]
    
    @staticmethod
    def weighted_choice(choices):
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
            if upto + w > r:
                return c
            upto += w
        assert False, "Shouldn't get here"
    
    @staticmethod
    def crossover(NN1,NN2, crossover_rate = .7):
        c1 = NN1.chromosome
        c2 = NN2.chromosome
        if random.random() < crossover_rate:
            position = random.randint(0, len(c1)-1)
            new_c1 = c1[:position] + c2[position:]
            new_c2 = c2[:position] + c1[position:]
            return Neural_Network(chromosome=new_c1), Neural_Network(chromosome=new_c2)
        return NN1,NN2
    
    @staticmethod
    def mutate(NN, mutation_rate = .2):
        c = NN.chromosome
        new_chromo = []
        for i in c:
            if random.random() < mutation_rate:
                a = i + np.random.uniform(-1,1) * .3
                new_chromo.append(a)
            else:
                new_chromo.append(i)
        return Neural_Network(chromosome = new_chromo)
    
    @staticmethod
    def create_next_gen(gen,population):
        next_gen = []
        individual_chance = [[i,i.get_fitness()] for i in gen]
        for _ in range(round(population/2)):
            parent1 = Neural_Network.weighted_choice(individual_chance)
            parent2 = Neural_Network.weighted_choice(individual_chance)
            parent1,parent2 = Neural_Network.crossover(parent1,parent2)
            parent1 = Neural_Network.mutate(parent1)
            parent2 = Neural_Network.mutate(parent2)
            next_gen += [parent1,parent2]
        return next_gen

def divide_if_not_zero(a, b):
    if b == 0:
        return 0
    else:
        return a / b

population = 10
gen = [Neural_Network() for _ in range(population)]
i = 0
sleep = False
best_score = 0
while 1:
    if i:
        avgs = [x - 11 for x in [j.fitness for j in gen]]
        print("AVERAGE: " + str( sum(avgs)/population))
        gen = Neural_Network.create_next_gen(gen, population)
    i += 1
    print("\n\nGENERATION: " + str(i))
    G.start()
    for x, NN in enumerate(gen):
        # print("GENOME: %s" % (NN.chromosome))
        print("SPECIES %s" % (str(x+1)))
        if sleep: time.sleep(1)
        done = False
        illegal_moves = 0
        zero_reward = 0
        NN.fitness += 10
        # print("AREA: %s" % G.area)
        while not done:
            X = []
            Max = max([math.log2(b) for b in [int(c) for c in [d.replace('0', '1') for d in [str(e) for f in G.area for e in f]]]])
            X.extend([divide_if_not_zero(a, Max) for a in [math.log2(b) for b in [int(c) for c in [d.replace('0', '1') for d in [str(e) for f in G.area for e in f]]]]])
            network_choice = NN.forward(X)
            move = False
            if G.is_stuck(G.area):
                done = True
                print("Stuck")
            if network_choice[0]:
                move = "up"
            elif network_choice[1]:
                move = "right"
            elif network_choice[2]:
                move = "down"
            elif network_choice[3]:
                move = "left"
            if move:
                if G.move(G.area, move)[1] == "blocked":
                    illegal_moves += 1
                    print("Moved %s, blocked" % move)
                else:
                    illegal_moves = 0
                    G.area, reward = G.move(G.area, move)
                    if reward == 0:
                        zero_reward += 1
                    else:
                        zero_reward = 0
                    NN.fitness += reward
                    print("Moved %s, reward: %s" % (move, reward))
                    if sleep: time.sleep(1)
                G.area = G.new_random(G.area)
            else:
                done = True
                print("Didn't move.")
                NN.fitness -= 10
            if illegal_moves >= 10:
                done = True
                print("Made too many illegal moves")
                NN.fitness -= 2
            if zero_reward >= 15:
                done = True
                print("Got zero reward too many times")
                NN.fitness -= 1
            if sleep: time.sleep(0.1)
        score = NN.fitness - 11
        print("SCORE: %s" % score)
        if score > best_score:
            print("New best score: %s" % score)
            best_score = score
        if sleep: time.sleep(1.5)
        G.reset()
