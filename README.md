## Install Nix
```bash
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
```

## Enter Nix development environment
```bash
nix develop
```

## Install Python dependencies
```bash
rye sync
```

## Activate Python environment
```bash
. .venv/bin/activate
```

For deactivating enter:
```bash
deactivate
```

## Check environment
```bash
btcli --help
```
