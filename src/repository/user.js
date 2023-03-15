import prisma from "../lib/prisma/client.js"

export const createUser = async (data) => {
	try {
		await prisma.user.create({
			data: {
				email: data.email,
				password: data.password,
				profile: {
					create: {
						name: data.profile.name,
						username: data.profile.username,
						graduation_year: data.profile.graduation_year,
						linkedin_url: data.profile.linkedin_url,
						twitter_username: data.profile.twitter_username
					}
				}
			}
		})
		return true
	}
	catch(err) {
		return false
	}
}

export const userExists = async (email) => {
	try {
		let count = await prisma.user.count({
			where: {
				email: email
			}
		})
		// console.log('count', count)
		if(count > 0) return true
		else return false
	}
	catch(err) {
		throw err
	}
}

export const getUserByEmail = async (email) => {
	try {
		let user = await prisma.user.findFirstOrThrow({
			where: {
				email: email
			},
			include: {
				profile: true
			}
		})
		return user
	}
	catch(err) {
		throw err
	}
}