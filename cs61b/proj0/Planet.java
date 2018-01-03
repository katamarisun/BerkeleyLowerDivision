/** Planet Class */
public class Planet {
	double xxPos;
	double yyPos;
	double xxVel;
	double yyVel;
	double mass;
	String imgFileName;
	/** Constructor for Planets with position, mass, and image name*/
	public Planet(double xP, double yP, double xV,
		double yV, double m, String img) {
		xxPos = xP;
		yyPos = yP;
		xxVel = xV;
		yyVel = yV;
		mass = m;
		imgFileName = img;
	}
	/** Creates a duplicate Planet*/
	public Planet(Planet p) {
		this.xxPos = p.xxPos;
		this.yyPos = p.yyPos;
		this.xxVel = p.xxVel;
		this.yyVel = p.yyVel;
		this.mass = p.mass;
		this.imgFileName = p.imgFileName;
	}
	/** Calculates the distance between two planets, takes in one planet*/
	public double calcDistance(Planet p) {
		double x_distance = p.xxPos - this.xxPos;
		double y_distance = p.yyPos - this.yyPos;
		double r_squared = x_distance * x_distance + y_distance * y_distance;
		return Math.sqrt(r_squared);
	}
	/** Method that takes in a planet as an argument and
	calculates the magnitude of the force between two planets*/
	public double calcForceExertedBy(Planet p){
		double distance = this.calcDistance(p);
		return (6.67 * Math.pow(10, -11)) * this.mass * p.mass / (distance * distance);
	}
	/** Methods that take in a planet and return 
	X and Y Component forces*/
	public double calcForceExertedByX(Planet p) {
		double distance = this.calcDistance(p);
		double force = this.calcForceExertedBy(p);
		return force * (p.xxPos - this.xxPos) / distance;
	}
	public double calcForceExertedByY(Planet p) {
		double distance = this.calcDistance(p);
		double force = this.calcForceExertedBy(p);
		return force * (p.yyPos - this.yyPos) / distance;
	}
	/** Methods taking in an array of planets and 
	returns the net force components applied*/
	public double calcNetForceExertedByX(Planet[] planets) {
		double net_force = 0;
		for (Planet body : planets) {
			if (!this.equals(body)) {
				net_force = net_force + this.calcForceExertedByX(body);
			}
		}
		return net_force;
	}
	public double calcNetForceExertedByY(Planet[] planets) {
		double net_force = 0;
		for (Planet body : planets) {
			if (!this.equals(body)) {
				net_force = net_force + this.calcForceExertedByY(body);
			}
		}
		return net_force;
	}
	/** Method that updates a planet's position, taking
	in the time and net forces*/
	public void update(double dt, double fX, double fY) {
		double x_accel = fX / this.mass;
		double y_accel = fY / this.mass;
		this.xxVel = this.xxVel + x_accel * dt;
		this.yyVel = this.yyVel + y_accel * dt;
		this.xxPos = this.xxPos + this.xxVel * dt;
		this.yyPos = this.yyPos + this.yyVel * dt;
	}
	public void draw() {
		StdDraw.picture(this.xxPos, this.yyPos, "images/" + this.imgFileName);
	}
}

