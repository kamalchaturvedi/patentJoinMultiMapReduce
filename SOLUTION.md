Lab3-PatentJoins
==================================

In this lab, we run a chain of Hadoop MR jobs, which combine different input data files using Reducer-Join, & help corelating the incoming data from these input sources to the required output.

Environment Setup
-----------------
I setup Dataproc cluster in Google Cloud environment with the following specs :
*    1 Master Node : 1 CPU, 3.5 GB RAM
*    2 Worker Nodes : 1 CPU, 3.5 GB RAM

Then, I created a git repository, & connected it to my local using ssh authentication. The same public key I added to Google Metadata, to be able to access git in compute instances. This also involved copying the private key to the compute instances to setup that git repository there.

Running the Code
-----------------
I have used the Python implementation, i.e. Hadoop Streaming with chained MR jobs to imprement Patent joins.

<code>cd PythonSolution</code>

<code>make</code>

Above commands run the jobs in the required sequence, to generate <i>stream-output-final</i> along with intermediate outputs.

Code Walkthrough
----------------
Mapper1 takes the two input files <i>cite75_99.txt</i> & <i>apat63_99.txt</i>, & outputs a stream of data from both. Reducer1 takes that data & outputs in the format
>   CITED CITING CITING_STATE

Now, passing this output & the <i>apat63_99.txt</i> to Mapper1 again will output a stream which when reduced by Reducer 2 give out output as
>   CITING CITING_STATE CITED CITED_STATE

This output when passed to CheckCitationCountMapper along with <i>apat63_99.txt</i> will output that stream, along with a stream of citations which come from the same state. This when evaluated by CheckCitationCountReducer will count those citations & add that count to the data present in <i>apat63_99.txt</i>.

Output
------

The output after running the hadoop-streaming job can be found in stream-output-final directory.
