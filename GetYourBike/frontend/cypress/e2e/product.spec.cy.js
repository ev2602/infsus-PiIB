describe('Product List', () => {
  it('displays a list of products', () => {
    cy.visit('http://localhost:3000')

    cy.intercept('GET', '/api/products/', [
      { id: 1, brand: 'Brand A' },
      { id: 2, brand: 'Brand B' },
    ]).as('getProducts');

    cy.wait('@getProducts');

    cy.contains('Brand A').should('be.visible');
    cy.contains('Brand B').should('be.visible');
  });
});
