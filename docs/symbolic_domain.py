from sphinx.domains import Domain
from sphinx.directives import ObjectDescription
from sphinx.roles import XRefRole

class SymbolicDirective(ObjectDescription):
    """Directive to describe a Symbolic language construct."""
    # Define the supported roles for this directive
    roles = ('keyword', 'symbol')

    def handle_signature(self, sig, signode):
        signode += signode.add_text(sig)
        return sig

class SymbolicDomain(Domain):
    """Custom Sphinx domain for the Symbolic language."""
    name = 'symbolic'
    label = 'Symbolic'
    object_types = {
        'keyword': SymbolicDirective,
        'symbol': SymbolicDirective,
    }
    roles = {
        'keyword': XRefRole(),
        'symbol': XRefRole(),
    }
    directives = {
        'keyword': SymbolicDirective,
        'symbol': SymbolicDirective,
    }
    initial_data = {}  # Required for custom domains

def setup(app):
    app.add_domain(SymbolicDomain)
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
