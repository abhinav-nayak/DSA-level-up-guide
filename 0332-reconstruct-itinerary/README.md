<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>332. Reconstruct Itinerary</title>
</head>
<body>

  <h1>332. Reconstruct Itinerary</h1>
  <p><strong>Status:</strong> Attempted</p>
  <p><strong>Difficulty:</strong> Hard</p>

  <h3>Topics</h3>
  <p>Graphs, Depth-First Search, Eulerian Path, Backtracking, Lexical Order</p>

  <h3>Problem Description</h3>
  <p>You are given a list of airline tickets where <code>tickets[i] = [from<sub>i</sub>, to<sub>i</sub>]</code> represent the departure and arrival airports of one flight. 
  Reconstruct the itinerary in order and return it.</p>

  <p>All of the tickets belong to a man who departs from <code>"JFK"</code>, thus the itinerary must begin with <code>"JFK"</code>. 
  If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.</p>

  <p>For example, the itinerary <code>["JFK", "LGA"]</code> has a smaller lexical order than <code>["JFK", "LGB"]</code>.</p>

  <p>You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.</p>

  <h2>Example 1:</h2>
  <pre>
Input:
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

Output:
["JFK","MUC","LHR","SFO","SJC"]
  </pre>

  <h2>Example 2:</h2>
  <pre>
Input:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

Output:
["JFK","ATL","JFK","SFO","ATL","SFO"]

Explanation:
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] 
but it is larger in lexical order.
  </pre>

  <h2>Constraints:</h2>
  <ul>
    <li>1 &le; tickets.length &le; 300</li>
    <li>tickets[i].length == 2</li>
    <li>from<sub>i</sub>.length == 3</li>
    <li>to<sub>i</sub>.length == 3</li>
    <li><code>from<sub>i</sub></code> and <code>to<sub>i</sub></code> consist of uppercase English letters.</li>
    <li><code>from<sub>i</sub> != to<sub>i</sub></code></li>
  </ul>

</body>
</html>
