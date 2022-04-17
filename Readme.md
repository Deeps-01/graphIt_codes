# My GraphIt Codes #
     GraphIt is a new domain-specific language that achieves high-performance
     across different algorithms, graphs, and architectures, while offering an easy-to-use
     high-level programming model. 
     
 <b> GraphIt decouples algorithms from performance optimizations (schedules) for graph applications to make it easy to            explore a large space
     of cache, NUMA, load balance, and data layout optimizations. As of now, GraphIt
     supports a wide range of applications, many different data structures, and numerous
     performance optimizations.
     
     
<hr>

# PageRank (PR) Algorithm #
     algorithm used by Google Search to rank web pages in their search engine results.


     
# Breadth First Search #
     
     BFS program written in the GraphIt algorithm language. GraphIt scheduling language input for optimizing the BFS algorithm
     is done through a hybrid traversal.
     

# Bucketing #
     Bucketing is generally used to exploit parallelism and maintain ordering in ordered graph algorithms.
     It is expressive enough to implement many parallel ordered
     graph algorithms. Existing frameworks support either lazy bucket update or eager bucket update approach.
     Bucketing data structure is used to maintain the execution ordering. Each bucket
     stores active vertices of the same priority, and the buckets are sorted in priority order. The program processes one
     bucket at a time in priority order and dynamically moves
     active vertices to new buckets when their priorities change.
     Updates to the bucket structure can be implemented using
     either an eager bucket update  approach or a lazy bucket
     update approach.



