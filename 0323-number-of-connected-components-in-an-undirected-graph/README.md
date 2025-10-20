<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Number of Connected Components in an Undirected Graph</title>
</head>
<body>

  <h1>Number of Connected Components in an Undirected Graph</h1>
  <p><strong>Status:</strong> Solved</p>

  <p>There is an undirected graph with <code>n</code> nodes. There is also an <code>edges</code> array, where <code>edges[i] = [a, b]</code> means that there is an edge between node <code>a</code> and node <code>b</code> in the graph.</p>
  <p>The nodes are numbered from <code>0</code> to <code>n - 1</code>.</p>
  <p>Return the total number of connected components in that graph.</p>

  <h2>Example 1:</h2>
  <pre>
Input:
n = 3  
edges = [[0,1], [0,2]]

Output:
1
  </pre>

  <h2>Example 2:</h2>
  <pre>
Input:
n = 6  
edges = [[0,1], [1,2], [2,3], [4,5]]

Output:
2
  </pre>

  <h2>Constraints:</h2>
  <ul>
    <li>1 &le; n &le; 100</li>
    <li>0 &le; edges.length &le; n * (n - 1) / 2</li>
  </ul>

</body>
</html>
