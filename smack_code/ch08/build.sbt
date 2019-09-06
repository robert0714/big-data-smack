name := "scala"
version := "0.98.5"
scalaVersion := "2.12.9"
crossScalaVersions := Seq("2.10.2", "2.10.3", "2.11.8","2.12.9")
libraryDependencies ++= Seq(
  "org.apache.kafka" %% "kafka" % "2.3.0",
  "junit"          % "junit"           % "4.12",
  "org.scalatest"  %% "scalatest"      % "3.0.1"
)