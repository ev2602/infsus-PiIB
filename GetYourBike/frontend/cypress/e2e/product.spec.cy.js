describe('Product List', () => {
  it('displays a list of rentbicycles', () => {
    cy.visit('http://localhost:3000/rent')

    cy.intercept('GET', '/api/rentBicycles/',[
      {
          "id": 8,
          "brand": "Trek",
          "model": "MT5647",
          "category": 1,
          "reservedDates": [
              "2024-05-28",
              "2024-05-29",
              "2024-05-30"
          ],
          "pricePerDay": 21.0
      },
      {
          "id": 9,
          "brand": "Specialized",
          "model": "H57287",
          "category": 2,
          "reservedDates": [
              "2024-05-23"
          ],
          "pricePerDay": 19.0
      }
  ]).as('getRentBicycles');

    cy.wait('@getRentBicycles');

    cy.contains('Specialized').should('be.visible');
    cy.contains('Trek').should('be.visible');
  });
});
