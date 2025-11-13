<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Alien Language Letter Order</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2rem; line-height: 1.6; }
    h1, h2 { color: #333; }
    pre { background: #f4f4f4; padding: 1rem; border-radius: 4px; overflow-x: auto; }
    code { background: #eef; padding: 0.2rem 0.4rem; border-radius: 3px; }
  </style>
</head>
<body>
  <h1>Alien Language Letter Order Problem</h1>

  <h2>Problem Statement</h2>
  <p>There is a foreign language which uses the Latin alphabet, but the order among letters is not “a”, “b”, “c” … “z” as in English.</p>

  <p>You receive a list of non-empty strings <code>words</code> from the dictionary, where the words are sorted lexicographically based on the rules of this new language.</p>

  <p>Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid orders of letters, you may return any of them.</p>

  <h3>Lexicographic Definition</h3>
  <p>A string <code>a</code> is lexicographically smaller than a string <code>b</code> if either:</p>
  <ul>
    <li>The first letter where they differ is smaller in <code>a</code> than in <code>b</code>.</li>
    <li><code>a</code> is a prefix of <code>b</code> and <code>a.length &lt; b.length</code>.</li>
  </ul>

  <h3>Examples</h3>

  <p><strong>Example 1:</strong></p>
  <pre>
Input: ["z","o"]  
Output: "zo"  
Explanation: From "z" and "o", we know 'z' &lt; 'o', so return "zo".
  </pre>

  <p><strong>Example 2:</strong></p>
  <pre>
Input: ["hrn","hrf","er","enn","rfnn"]  
Output: "hernf"  
Explanation:
from "hrn" and "hrf", we know 'n' &lt; 'f'  
from "hrf" and "er", we know 'h' &lt; 'e'  
from "er" and "enn", we know 'r' &lt; 'n'  
from "enn" and "rfnn", we know 'e' &lt; 'r'  
so one possible solution is "hernf"
  </pre>

  <h3>Constraints</h3>
  <ul>
    <li>The input words will contain characters only from lowercase ‘a’ to ‘z’.</li>
    <li>1 &le; words.length &le; 100</li>
    <li>1 &le; words[i].length &le; 100</li>
  </ul>

  <h3>Solution Approach</h3>
  <p>Model the problem as a directed graph where each unique character is a node, and the relative ordering between two characters (deduced from adjacent words) represents a directed edge. Use a topological sort (e.g., via DFS or Kahn’s algorithm) to derive a valid letter ordering or detect an invalid ordering (cycle or prefix contradiction). :contentReference[oaicite:0]{index=0}</p>

  <h3>Time &amp; Space Complexity</h3>
  <ul>
    <li>Time Complexity: <code>O(N + V + E)</code> — where <code>N</code> is the sum of lengths of all the strings, <code>V</code> is the number of unique characters, and <code>E</code> is the number of edges (ordering constraints) in the graph. :contentReference[oaicite:1]{index=1}</li>
    <li>Space Complexity: <code>O(V + E)</code> — due to storing the adjacency list and auxiliary structures for traversal. :contentReference[oaicite:2]{index=2}</li>
  </ul>

  <h3>Code Snippet</h3>
  <pre><code>
// (Pseudo-code showing high-level steps)
build adjacency list from comparisons of adjacent words
detect invalid prefix case (e.g., longer word before its prefix)
perform topological sort (or detect cycle)
return the ordering string or "" if invalid
  </code></pre>

  <h3>Usage</h3>
  <p>Pass the list of words to the function, then print or return the derived letter ordering. Handle edge cases where no valid ordering exists by returning an empty string <code>""</code>.</p>

  <h3>License &amp; Credits</h3>
  <p>Based on the classic “Alien Dictionary” problem and topological sort techniques.</p>
</body>
</html>
