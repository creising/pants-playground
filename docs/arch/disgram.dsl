workspace {
  model {
    user = person "User" "The user"
    softwareSystem = softwareSystem "Demo App" "My first system" {
        apiModule = container "API" {
            user -> this "Uses"
            tags "Application"
        }
        
        container "Fact Service" {
            apiModule -> this "Requets facts"
        }
    }
  }

  views {
    container softwareSystem {
      include *
      autolayout lr
    }
    theme default
  }
}