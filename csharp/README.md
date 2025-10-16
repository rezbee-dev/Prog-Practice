# C# Notes

## How To

**Setup**
- Install VS Code w/ "C# Dev Kit" extension
- Create console app: `dotnet new console --name "MyFirstConsoleApp"`

**Common commands**
- `dotnet run`: builds and executes the app
- `dotnet build`: compiles project and dependencies into exe. or library
- `dotnet clean`: deletes output directories `bin` and `obj` to ensure fresh build
- `dotnet add <package>`: adds NuGet package reference to project file `.csproj`
- `dotnet remove <package>`: removes NuGet package reference from project file
- `dotnet restore`: resolves and downloads project dependencies that are specified in project file
  - implicitly run in `build` and `run` commands
- `dotnet publish`: compiles the app and deps into deployable folder for final executable for distribution
