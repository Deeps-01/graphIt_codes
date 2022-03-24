func updateEdge(src:Vertex, dest: Vertex)
  latest_rank[dest]= + oldrank[src]/outdeg[src];
end

func updateVertex(v:Vertex)
  latest_rank[v]=beta + 0.85*latest_rank[v];
  oldrank[v]=latest_rank[v];
  latest_rank[v]=0;
end

func main()
  for i in 1:max
      #s1#edges.apply(updateEdge);
     vertices.apply(updateVertex);
  end
end


schedule:
  program->configApplyDirection("s1","SparsePush");
  program->configApplyParallelization("s1","dynamic-vertex-parallel");
