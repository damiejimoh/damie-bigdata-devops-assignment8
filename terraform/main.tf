terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"
}

# Create a Docker network for Hadoop cluster
resource "docker_network" "hadoop_network" {
  name = "hadoop_network"
}

# NameNode Container
resource "docker_container" "namenode" {
  name  = "hadoop-namenode"
  image = "bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8"
  
  networks_advanced {
    name    = docker_network.hadoop_network.name
    aliases = ["namenode"]  # Critical: allows other containers to resolve "namenode"
  }
  
  ports {
    internal = 9870
    external = 9870
  }
  
  ports {
    internal = 9000
    external = 9000
  }
  
  env = [
    "CLUSTER_NAME=hadoop-cluster",
    "CORE_CONF_fs_defaultFS=hdfs://namenode:9000"
  ]
}

# DataNode Container
resource "docker_container" "datanode" {
  name  = "hadoop-datanode"
  image = "bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8"
  
  networks_advanced {
    name    = docker_network.hadoop_network.name
    aliases = ["datanode"]  # Critical: allows other containers to resolve "datanode"
  }
  
  ports {
    internal = 9864
    external = 9864
  }
  
  env = [
    "CORE_CONF_fs_defaultFS=hdfs://namenode:9000",
    "SERVICE_PRECONDITION=namenode:9870"
  ]
  
  depends_on = [docker_container.namenode]
}

# ResourceManager Container
resource "docker_container" "resourcemanager" {
  name  = "hadoop-resourcemanager"
  image = "bde2020/hadoop-resourcemanager:2.0.0-hadoop3.2.1-java8"
  
  networks_advanced {
    name    = docker_network.hadoop_network.name
    aliases = ["resourcemanager"]  # Critical: allows other containers to resolve "resourcemanager"
  }
  
  ports {
    internal = 8088
    external = 8088
  }
  
  env = [
    "CORE_CONF_fs_defaultFS=hdfs://namenode:9000",
    "SERVICE_PRECONDITION=namenode:9870 datanode:9864"
  ]
  
  depends_on = [docker_container.namenode, docker_container.datanode]
}

# Outputs
output "namenode_ui" {
  value       = "http://localhost:9870"
  description = "Hadoop NameNode Web UI"
}

output "datanode_ui" {
  value       = "http://localhost:9864"
  description = "Hadoop DataNode Web UI"
}

output "resourcemanager_ui" {
  value       = "http://localhost:8088"
  description = "Hadoop ResourceManager Web UI (YARN)"
}