describe('Rent Bicycles Page Integration Test', () => {
    beforeEach(() => {
      cy.visit('http://localhost:3000/rent');
    })
  
    it('fetches and displays rent bicycles from the backend', () => {
      cy.intercept('GET', '/api/rentBicycles/').as('getRentBicycles');

      cy.wait('@getRentBicycles').then((interception) => {
        expect(interception.response.statusCode).to.eq(200);

        expect(interception.request.url).to.include('/api/rentBicycles/');
  
        expect(interception.response.body).to.be.an('array');
        expect(interception.response.body[0]).to.have.property('brand');
      });

      cy.contains('Trek').should('be.visible');
      cy.contains('MT5647').should('be.visible');
      cy.contains('21').should('be.visible');
    })
  })
  