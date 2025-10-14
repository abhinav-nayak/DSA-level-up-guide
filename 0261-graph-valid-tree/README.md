<h2><a href="https://leetcode.com/problems/graph-valid-tree">261. Graph Valid Tree</a></h2>
<h3>Medium</h3>
<hr>
<p>Given <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code> and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.</p>

<p><strong>Note:</strong></p>
<ul>
  <li>You can assume that no duplicate edges will appear in <code>edges</code>.</li>
  <li>Since all edges are undirected, <code>[0, 1]</code> is the same as <code>[1, 0]</code> and thus will not appear together in <code>edges</code>.</li>
</ul>

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
<strong>Output:</strong> false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 &lt;= n &lt;= 100</code></li>
  <li><code>0 &lt;= edges.length &lt;= n * (n - 1) / 2</code></li>
</ul>
