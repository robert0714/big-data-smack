name := "ch08"
version := "0.1"
scalaVersion := "2.12.9"
libraryDependencies += "org.apache.kafka" %% "kafka" % "0.10.2.2"
// libraryDependencies += "org.apache.kafka" %% "kafka" % "2.1.1"

// https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients
libraryDependencies += "org.apache.kafka" % "kafka-clients" % "0.10.0.0"

resolvers += Resolver.mavenLocal