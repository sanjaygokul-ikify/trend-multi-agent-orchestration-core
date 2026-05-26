import argparse
from packages.core import Engine
from packages.services import orchestrator

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', action='store_true')
    parser.add_argument('--stop', action='store_true')
    args = parser.parse_args()
    
    engine = Engine(None, None, None, None)
    orchestrator = orchestrator.Orchestrator(engine)
    
    if args.start:
        orchestrator.start()
    elif args.stop:
        orchestrator.stop()