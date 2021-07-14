hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-D mapreduce.job.name="WordCount Job via Streaming" \
-input /tmp/test.txt \
-output /tmp/WordCount \
-mapper /home/vlad/mapper.py \
-combiner /home/vlad/reducer.py \
-reducer /home/vlad/reducer.py