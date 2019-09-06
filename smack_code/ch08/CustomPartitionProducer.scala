package apress.ch08

import java.util.Date
import java.util.Properties
import java.util.Random
import org.apache.kafka.clients.producer.KafkaProducer
import org.apache.kafka.clients.producer.ProducerRecord
import CustomPartitionProducer._

object CustomPartitionProducer {

  var producer: KafkaProducer[String, String] = _

  def main(args: Array[String]) {
    val argsCount = args.length
    if (argsCount == 0 || argsCount == 1)
      throw new IllegalArgumentException(
        "Please provide topic name and Message count as arguments")

    // Topic name and the message count to be published is passed from the
    // command line
    val topic = args(0)
    val count = args(1)
    val messageCount = java.lang.Integer.parseInt(count)
    println("Topic Name - " + topic)
    println("Message Count - " + messageCount)
    val simpleProducer = new CustomPartitionProducer()
    simpleProducer.publishMessage(topic, messageCount)
  }
}

class CustomPartitionProducer {

  val props = new Properties()

  // Set the broker list for requesting metadata to find the lead broker
  props.put("metadata.broker.list",
    "107.170.38.238:9092, 107.170.38.238:9093, 107.170.38.238:9094")

  // This specifies the serializer class for keys
  props.put("serializer.class", "kafka.serializer.StringEncoder")

  // Defines the class to be used for determining the partition
  // in the topic where the message needs to be sent.
  props.put("partitioner.class", "apress.ch08.SimplePartitioner")

  // 1 means the producer receives an acknowledgment once the lead replica
  // has received the data. This option provides better durability as the
  // client waits until the server acknowledges the request as successful.
  props.put("request.required.acks", "1")

  producer = new KafkaProducer(props)

  private def publishMessage(topic: String, messageCount: Int) {
    val random = new Random()
    for (mCount <- 0 until messageCount) {
      val clientIP = "107.170.38." + random.nextInt(255)
      val accessTime = new Date().toString
      val msg = accessTime + ",kafka.apache.org," + clientIP
      println(msg)
      // Create a ProducerRecord instance
      val data = new ProducerRecord[String, String](topic, clientIP, msg)

      // Publish the message
      producer.send(data)
    }
    producer.close()
  }
}
