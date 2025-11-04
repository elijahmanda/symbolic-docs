from sphinx.domains import Domain
from sphinx.directives import ObjectDescription
from sphinx.roles import XRefRole
from sphinx import addnodes
from docutils import nodes

class SymbolicDirective(ObjectDescription):
    """Directive to describe a Symbolic language construct."""
    
    # Add CSS classes for better styling
    def add_target_and_index(self, name, sig, signode):
        super().add_target_and_index(name, sig, signode)
        # Add specific CSS classes based on object type
        if self.objtype == 'keyword':
            signode['classes'].append('symbolic-keyword')
        elif self.objtype == 'symbol':
            signode['classes'].append('symbolic-symbol')

class SymbolicXRefRole(XRefRole):
    """Enhanced cross-reference role with better styling."""
    
    def process_link(self, env, refnode, has_explicit_title, title, target):
        # Add CSS classes to cross-references
        if not has_explicit_title:
            if refnode['reftype'] == 'keyword':
                title = f"keyword:{title}"
            elif refnode['reftype'] == 'symbol':
                title = f"symbol:{title}"
        return title, target

class SymbolicDomain(Domain):
    """Custom Sphinx domain for the Symbolic language with enhanced visibility."""
    
    name = 'symbolic'
    label = 'Symbolic'
    
    object_types = {
        'keyword': {'name': 'keyword', 'roles': ('keyword',), 'attrs': {'class': 'symbolic-keyword'}},
        'symbol': {'name': 'symbol', 'roles': ('symbol',), 'attrs': {'class': 'symbolic-symbol'}},
    }
    
    roles = {
        'keyword': SymbolicXRefRole(),
        'symbol': SymbolicXRefRole(),
    }
    
    directives = {
        'keyword': SymbolicDirective,
        'symbol': SymbolicDirective,
    }
    
    initial_data = {
        'keywords': {},
        'symbols': {},
    }

def setup(app):
    app.add_domain(SymbolicDomain)
    
    # Add CSS for better syntax highlighting visibility
    app.add_css_file('symbolic.css')
    
    return {
        'version': '1.0', 
        'parallel_read_safe': True, 
        'parallel_write_safe': True
    }

