#include <limits.h>
#include <stdio.h>
#include <stdlib.h>


int main(int argc, int argv[]) {
	
	
	int cost(int cities[][2], int city1, int city2) {
		
		int x1 = cities[city1][1];
		int y1 = cities[city1][2];
		int x2 = cities[city2][1];
		int y2 = cities[city2][2];
		
		float a = (x2 - x1)^2;
		float b = (y2 - y1)^2;
		
		return (a + b)^0.5;
	}
	
	int* findRoute(int cities[][2], int numCities, int startCity) {
		
		
		int* currentRoute = (int*) malloc(sizeof(int) * numCities);
		int* cheapestRoute = (int*) malloc(sizeof(int) * numCities);
		int currentCity = startCity;
		int cheapestCity;
		int currentCost = INT_MAX;
		int totalCost = 0;
		int city, i, minCost;
		
		
		int* citiesToCheck = (int*) malloc(sizeof(int) * numCities);
		for (i = 0; i < numCities; i++) {
			citiesToCheck[i] = i;
		}
		
		

		/* Iterate over all the cities */
		for (currentCity = 1; currentCity < numCities; currentCity++) {
			cheapestCity = INT_MAX;
			minCost = INT_MAX;
			
			
			/* Find the city closest to the current city */
			for (city = 0; city < numCities; city++) {
				
				if (citiesToCheck[city] == -1)
					continue;
				
				
				currentCost = cost(cities, currentCity, city);
				
				if (currentCost < minCost) {
					minCost = currentCost;
					totalCost += currentCost;
					cheapestCity = city;
				}
				
				citiesToCheck[city] = -1;
			}
			
			cheapestRoute[0] = totalCost;
			cheapestRoute[currentCity] = cheapestCity;	
		}
		
		return cheapestRoute
	}

		

	/* for each city, cities[][] holds an x and y coordinate */
	int* greedyTsp(int cities[][2], int numCities) {
		
		
		/* The first number in currentRoute is the cost of the route.
			The subsequent numbers represent the sequence of cities visited. */
		int* currentRoute = (int*) malloc(sizeof(int) * numCities);
		int* cheapestRoute = (int*) malloc(sizeof(int) * numCities);
		int minCost = INT_MAX;
		int currentCost;
		int city;
				
		for (city = 0; city < numCities; city++) {
			currentRoute = findRoute(cities, numCities, city);
			currentCost = currentRoute[0];
				
			if (currentCost < minCost) {
				minCost = currentCost;
				cheapestRoute = currentRoute;
			}
		}
			
		return cheapestRoute;
	}
}

