class Solution:
    #time: Ov+Oe
    #space:Ov
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indeg = defaultdict(int) #for every recipes, how many ingredients we need
        graph = defaultdict(list) 


        for recipe, ingredient in zip (recipes,ingredients):
            indeg[recipe] = len(ingredient) # for every,recipe, we need this number of the indegred
            for ing in ingredient:
                graph[ing].append(recipe)  # This ingredient is used in this recipe


        ans = [] #ouput , which recipe that we can make

        queue = deque(supplies)
        recipes = set(recipes)

        while queue:
            x = queue.popleft()
            if x in recipes:
                ans.append(x)
            for xx in graph[x]:
                indeg[xx] -= 1
                if indeg[xx] == 0:
                    queue.append(xx)
        return ans
        
          


        