<h2><a href="https://neetcode.io/problems/islands-and-treasure?list=neetcode150">Islands and Treasure</a></h2><h3>Medium</h3><hr>
<p>You are given a 2D grid representing a map of islands, treasures, and water. Each cell of the grid can be one of the following:</p>

<ul>
  <li><code>-1</code> representing water (impassable).</li>
  <li><code>0</code> representing a treasure.</li>
  <li><code>INF</code> (2147483647) representing land where the distance to the nearest treasure is not yet known.</li>
</ul>

<p>Your task is to fill each <code>INF</code> cell with the distance to its nearest treasure. If a treasure is unreachable, the cell should remain <code>INF</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
grid = [
  [INF, -1,  0, INF],
  [INF, INF, INF, -1],
  [INF, -1, INF, -1],
  [0,   -1, INF, INF]
]

<strong>Output:</strong>
grid = [
  [3, -1, 0,  1],
  [2,  2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3,  4]
]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
  <li><code>m == grid.length</code></li>
  <li><code>n == grid[i].length</code></li>
  <li><code>1 &lt;= m, n &lt;= 100</code></li>
  <li><code>grid[i][j] ∈ { -1, 0, INF }</code></li>
</ul>

<p>&nbsp;</p>
<p><b>Follow up:</b></p>
<ul>
  <li>Can you solve this efficiently using <strong>multi-source BFS</strong> starting from all treasures?</li>
  <li>What would be the time and space complexity of your solution?</li>
</ul>
