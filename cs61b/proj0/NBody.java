public class NBody {
	public static double readRadius(String file_name) {
		In in = new In(file_name);
		in.readDouble();
		return in.readDouble();
	}
	public static Planet[] readPlanets(String file_name) {
		In input = new In(file_name);
		Planet[] planets = new Planet[input.readInt()];
		input.readDouble(); // skips the universe radius
		for(int i = 0; i < planets.length; i++) {
			planets[i] = new Planet(input.readDouble(), input.readDouble(), input.readDouble(), 
				input.readDouble(), input.readDouble(), input.readString());
		}
		return planets;
	}
	public static void main(String[] args) {
		double T = Double.parseDouble(args[0]);
		double dt = Double.parseDouble(args[1]);
		/** Reads in file data on planets*/
		String filename = args[2];
		double radius = readRadius(filename);
		Planet[] planets = readPlanets(filename);
		/** Draws the initial positions of the planets*/
		StdDraw.setScale(-radius, radius);
		StdDraw.picture(0, 0, "images/starfield.jpg");
		for (Planet body : planets) {
			body.draw();
		}
		/** Update loop that displays the motion of planets*/
		StdAudio.play("audio/2001.mid");
		double time = 0;
		while (time < T) {
			double[] xForces = new double[planets.length];
			double[] yForces = new double[planets.length];
			for (int i = 0; i < planets.length; i ++) {
				xForces[i] = planets[i].calcNetForceExertedByX(planets);
				yForces[i] = planets[i].calcNetForceExertedByY(planets);
			}
			for (int i = 0; i < planets.length; i ++) {
				planets[i].update(dt, xForces[i], yForces[i]);
			}
			StdDraw.picture(0, 0, "images/starfield.jpg");
			for (Planet body : planets) {
				body.draw();
			}
			StdDraw.show(10);
			time += dt;
		}
		StdOut.printf("%d\n", planets.length);
		StdOut.printf("%.2e\n", radius);
		for (int i = 0; i < planets.length; i++) {
			StdOut.printf("%11.4e %11.4e %11.4e %11.4e %11.4e %12s\n",
   			planets[i].xxPos, planets[i].yyPos, planets[i].xxVel, planets[i].yyVel, planets[i].mass, planets[i].imgFileName);	
		}
	}
}
