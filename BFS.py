element Vertex end
 element Edge end
 const edges : edgeset{Edge}(Vertex,Vertex)
 = load(argv[1]);
 const vertices : vertexset{Vertex}
 = edges.getVertices();
 const parent : vector{Vertex}(int) = -1;

 func toFilter(v : Vertex) -> output : bool
 output = (parent[v] == -1);
 end

 func updateEdge(src : Vertex, dst : Vertex)
 parent[dst] = src;
 end

 func main()
 var frontier : vertexset{Vertex}
 = new vertexset{Vertex}(0);
 var start_vertex : int = atoi(argv[2]);
 frontier.addVertex(start_vertex);
 parent[start_vertex] = start_vertex;
 #s0# while (frontier.getVertexSetSize() != 0)
 #s1# var output : vertexset{Vertex} =
 edges.from(frontier).to(toFilter).
 applyModified(updateEdge, parent, true);
 delete frontier;
 frontier = output;
 end
 delete frontier;
 end

 
 
 configApplyDirection("s0:s1", "DensePull-SparsePush")
 configApplyDenseVertexSet("s0:s1", "src-vertexset",
 "bitvector", "DensePull")
 configApplyParallelization("s0:s1",
 "dynamic-vertex-parallel")
